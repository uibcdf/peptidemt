"""Test case interpretation and saved integrity using artificial arrays only."""

import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

SPEC = importlib.util.spec_from_file_location(
    "mdm2_t0", Path(__file__).resolve().parents[1] / "mdm2_t0.py"
)
CASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CASE)


def observations():
    views = {
        name: {"receptor_rmsd_nm": 0.0, "peptide_rmsd_nm": value}
        for name, value in (("reference", 0.0), ("rigid", 0.0), ("displaced", 10.0))
    }
    base = np.array([[[0.30, 0.46], [0.41, 0.80]]])
    arrays = {
        name + "_distances": base.copy() + offset
        for name, offset in (("reference", 0.0), ("rigid", 0.0), ("displaced", 10.0))
    }
    for name in views:
        for threshold in CASE.THRESHOLDS:
            arrays[f"{name}_contacts_{round(threshold * 100):03d}"] = (
                arrays[name + "_distances"] <= threshold
            )
    return views, arrays


def test_fixed_artificial_observations_pass():
    views, arrays = observations()
    assert all(CASE.compare_views(views, arrays).values())


def test_independent_peptide_refit_cannot_erase_displacement():
    views, arrays = observations()
    views["displaced"]["peptide_rmsd_nm"] = 0.0
    assert CASE.compare_views(views, arrays)["displaced_peptide_rmsd"] is False


def test_rigid_distance_drift_and_spurious_contacts_are_rejected():
    views, arrays = observations()
    arrays["rigid_distances"][0, 0, 0] += 0.01
    arrays["displaced_contacts_045"][0, 0, 0] = True
    checks = CASE.compare_views(views, arrays)
    assert checks["rigid_distances_preserved"] is False
    assert checks["displaced_no_contacts_045"] is False
    assert checks["displaced_contact_definition_045"] is False


def test_threshold_boundary_band_does_not_demand_invariance():
    views, arrays = observations()
    arrays["reference_distances"][0, 0, 0] = 0.45 + CASE.TOLERANCE / 4
    arrays["rigid_distances"][0, 0, 0] = 0.45 - CASE.TOLERANCE / 4
    for name in ("reference", "rigid"):
        for threshold in CASE.THRESHOLDS:
            arrays[f"{name}_contacts_{round(threshold * 100):03d}"] = (
                arrays[name + "_distances"] <= threshold
            )
    assert all(CASE.compare_views(views, arrays).values())


@pytest.mark.parametrize(
    "damage", ("missing-view", "missing-array", "bad-shape", "nan")
)
def test_incomplete_or_invalid_evidence_cannot_pass(damage):
    views, arrays = observations()
    if damage == "missing-view":
        del views["displaced"]
    elif damage == "missing-array":
        del arrays["rigid_contacts_040"]
    elif damage == "bad-shape":
        arrays["rigid_distances"] = np.zeros((2, 2))
    else:
        arrays["reference_distances"][0, 0, 0] = np.nan
    assert not all(CASE.compare_views(views, arrays).values())


def saved_report(directory):
    # Inspection checks file identity, not scientific recomputation or npz parsing.
    path = directory / "arrays.npz"
    path.write_bytes(b"artificial integrity fixture")
    result = {
        "case": "MDM2-p53 T0",
        "entry": "1YCR",
        "revision": [1, 5],
        "pbc": False,
        "passed": True,
        "checks": {"artificial_fixture": True},
        "thresholds": {"value": list(CASE.THRESHOLDS), "unit": "nm", "primary": 0.45},
        "tolerance": {"value": CASE.TOLERANCE, "unit": "nm"},
        "array_file": CASE.identity(path),
        "arrays": {"reference_distances": {"unit": "nm"}},
    }
    (directory / "result.json").write_text(json.dumps(result))
    return result


def test_saved_inspection_detects_changed_artifact_without_providers(tmp_path):
    saved_report(tmp_path)
    assert CASE.inspect(tmp_path)["new_geometry_operations"] == 0
    (tmp_path / "arrays.npz").write_bytes(b"changed fixture")
    with pytest.raises(ValueError, match="artifact changed"):
        CASE.inspect(tmp_path)


def test_saved_unit_or_criterion_changes_are_rejected(tmp_path):
    result = saved_report(tmp_path)
    result["tolerance"]["unit"] = "angstrom"
    (tmp_path / "result.json").write_text(json.dumps(result))
    with pytest.raises(ValueError, match="fixed T0 definitions"):
        CASE.inspect(tmp_path)


def test_unqualified_profile_blocks_before_molecular_import_or_worker(tmp_path):
    (tmp_path / "profile-qualification.json").write_text(
        json.dumps({"passed": False, "source_ref": CASE.OWNER_REF})
    )
    with pytest.raises(ValueError, match="has not passed"):
        CASE.run(tmp_path)
    assert list(tmp_path.iterdir()) == [tmp_path / "profile-qualification.json"]
