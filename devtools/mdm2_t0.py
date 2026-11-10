"""Run the approved, single-reference MDM2 T0 development case (D51).

Molecular operations belong to MolSysMT. This is a case coordinator, not a
binding predictor or a public PeptideMT molecular-system API. See the work order.
"""

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import resource
import shutil
import sys
import tempfile
import traceback
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OWNER_REF = "ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6"
THRESHOLDS = (0.40, 0.45, 0.50)
TOLERANCE = 1e-6
LIMITS = dict(
    min_available_memory_bytes=4 * 1024**3,
    min_free_disk_bytes=1024**3,
    threads=1,
    wall_seconds=180,
    rss_stop_bytes=2 * 1024**3,
    max_output_bytes=64 * 1024**2,
)
SOURCES = (
    (
        "revision.html",
        "https://www.rcsb.org/versions/1YCR",
        1024**2,
    ),
    ("entry.html", "https://www.rcsb.org/structure/1YCR", 1024**2),
    (
        "usage.html",
        "https://www.wwpdb.org/about/usage-policies",
        1024**2,
    ),
    (
        "1ycr-v1-5.cif.gz",
        "https://files-versioned.rcsb.org/pdb_versioned/data/entries/yc/"
        "pdb_00001ycr/pdb_00001ycr_xyz_v1-5.cif.gz",
        2 * 1024**2,
    ),
    (
        "1ycr-validation.pdf",
        "https://files.rcsb.org/validation/view/1ycr_full_validation.pdf",
        2 * 1024**2,
    ),
)


def identity(path):
    path = Path(path).resolve()
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def write(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def supervision():
    spec = importlib.util.spec_from_file_location(
        "t0_supervision", ROOT / "src/peptidemt/_hydramp_process.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def acquire(task):
    """Receive bounded public bytes; molecular interpretation is a later step."""
    from datetime import datetime, timezone

    directory = task / "source"
    directory.mkdir()
    records = []
    try:
        for name, url, limit in SOURCES:
            record = {"name": name, "requested_url": url}
            records.append(record)
            try:
                request = Request(url, headers={"User-Agent": "PeptideMT-T0/1"})
                with urlopen(request, timeout=25) as response:
                    data = response.read(limit + 1)
                    if len(data) > limit:
                        raise ValueError("Source exceeds its acquisition byte limit")
                    record.update(
                        received_at_utc=datetime.now(timezone.utc).isoformat(),
                        final_url=response.url,
                        status=response.status,
                        content_type=response.headers.get("Content-Type"),
                        last_modified=response.headers.get("Last-Modified"),
                    )
                path = directory / name
                with path.open("xb") as stream:
                    stream.write(data)
                record.update(identity(path))
                if name.endswith(".gz"):
                    with gzip.open(path, "rb") as stream:
                        expanded = stream.read(8 * 1024**2 + 1)
                    if len(expanded) > 8 * 1024**2:
                        raise ValueError("Expanded source exceeds 8 MiB")
                    expanded_path = directory / "1ycr-v1-5.cif"
                    with expanded_path.open("xb") as stream:
                        stream.write(expanded)
                    record["expanded"] = identity(expanded_path)
            except Exception as exc:
                record["failure"] = {"type": type(exc).__name__, "message": str(exc)}
                if name != "1ycr-validation.pdf":
                    raise
            if sum(p.stat().st_size for p in directory.iterdir()) > 32 * 1024**2:
                raise ValueError("Source package exceeds 32 MiB")
    finally:
        write(
            directory / "manifest.json",
            {"sources": records, "expected_entry": "1YCR", "expected_revision": [1, 5]},
        )
    return records


def source_rows(container, category):
    """Read metadata from the public parser object returned by MolSysMT."""
    obj = container.getObj(category)
    if obj is None:
        return []
    names = obj.getAttributeList()
    return [dict(zip(names, row, strict=True)) for row in obj.getRowList()]


def compare_views(views, arrays):
    """Compare owner-returned arrays using only the fixed T0 criteria."""
    import numpy as np

    checks = {"exact_three_views": set(views) == {"reference", "rigid", "displaced"}}
    expected_keys = {
        name + suffix
        for name in ("reference", "rigid", "displaced")
        for suffix in ("_distances", "_contacts_040", "_contacts_045", "_contacts_050")
    }
    checks["required_arrays_present"] = expected_keys <= set(arrays)
    if not all(checks.values()):
        return checks
    base = arrays["reference_distances"]
    checks["finite_nonempty_distances"] = bool(
        base.size and base.ndim == 3 and base.shape[0] == 1 and np.isfinite(base).all()
    )
    checks["reference_contact_present"] = bool(arrays["reference_contacts_045"].any())
    for name, metrics in views.items():
        checks[name + "_receptor_fit"] = metrics["receptor_rmsd_nm"] <= TOLERANCE
        expected = 10.0 if name == "displaced" else 0.0
        checks[name + "_peptide_rmsd"] = (
            abs(metrics["peptide_rmsd_nm"] - expected) <= TOLERANCE
        )
        distances = arrays[name + "_distances"]
        checks[name + "_distances_finite_same_shape"] = bool(
            distances.shape == base.shape and np.isfinite(distances).all()
        )
        if distances.shape != base.shape:
            continue
        if name == "rigid":
            checks["rigid_distances_preserved"] = bool(
                np.allclose(distances, base, atol=TOLERANCE, rtol=0)
            )
        for threshold in THRESHOLDS:
            suffix = f"{round(threshold * 100):03d}"
            contacts = arrays[name + "_contacts_" + suffix]
            # Enforce the inclusive owner definition as well as invariance.
            checks[f"{name}_contact_definition_{suffix}"] = bool(
                contacts.dtype == np.bool_
                and contacts.shape == distances.shape
                and np.array_equal(contacts, distances <= threshold)
            )
            if contacts.shape != distances.shape:
                continue
            if name == "displaced":
                checks["displaced_no_contacts_" + suffix] = not bool(contacts.any())
            elif name == "rigid":
                outside = np.abs(base - threshold) > TOLERANCE
                checks["rigid_contacts_preserved_" + suffix] = bool(
                    np.array_equal(
                        contacts[outside],
                        arrays["reference_contacts_" + suffix][outside],
                    )
                )
    return checks


def geometry(task, directory):
    """Receive/measure through MolSysMT; preserve the raw reference unchanged."""
    import numpy as np
    import pyunitwizard as puw

    # A non-default application policy exercises explicit nm extraction.
    with puw.context(standard_units=["angstrom", "ps", "radian"]):
        import molsysmt as msm

        source = task / "source/1ycr-v1-5.cif"
        received = json.loads((task / "source/manifest.json").read_text())
        source_record = next(r for r in received["sources"] if "expanded" in r)
        if identity(source) != source_record["expanded"]:
            raise ValueError("Coordinate source changed since acquisition")
        container = msm.convert(
            str(source), to_form="mmcif.PdbxContainers.DataContainer"
        )
        metadata = {
            key: source_rows(container, key)
            for key in (
                "entry",
                "pdbx_audit_revision_history",
                "entity",
                "entity_poly",
                "struct_asym",
                "pdbx_struct_assembly",
                "pdbx_struct_assembly_gen",
                "pdbx_struct_oper_list",
                "cell",
                "symmetry",
            )
        }
        atom_rows = source_rows(container, "atom_site")
        source_models = sorted(
            {row.get("pdbx_PDB_model_num", "?") for row in atom_rows}
        )
        metadata["observed_source_model_ids"] = source_models
        write(directory / "source-metadata.json", metadata)
        if [r["id"] for r in metadata["entry"]] != ["1YCR"]:
            raise ValueError("Unexpected source entry identity")
        versions = [
            (int(r["major_revision"]), int(r["minor_revision"]))
            for r in metadata["pdbx_audit_revision_history"]
        ]
        if not versions or max(versions) != (1, 5):
            raise ValueError("Unexpected source revision")
        if len(source_models) != 1 or source_models[0] in {"?", "."}:
            raise ValueError("Ambiguous or absent source coordinate-model identity")
        system, conversion_report = msm.convert(
            str(source), to_form="molsysmt.MolSys", return_report=True
        )
        write(directory / "conversion-report.json", asdict(conversion_report))
        if msm.get(system, n_structures=True) != 1:
            raise ValueError("T0 requires exactly one represented structure")

        def get(element="system", selection="all", **attribute):
            return msm.get(system, element=element, selection=selection, **attribute)

        def numeric(quantity):
            return np.asarray(puw.get_value(quantity, to_unit="nm"), dtype=np.float64)

        chain_ids = list(get("chain", chain_id=True))
        chain_names = list(get("chain", chain_name=True))
        entities = {
            row["id"]: row["pdbx_description"].strip().upper()
            for row in metadata["entity"]
        }
        chains = {row["id"]: row["entity_id"] for row in metadata["struct_asym"]}
        if (
            len(chain_ids) != 2
            or entities.get(chains.get("A")) != "MDM2"
            or entities.get(chains.get("B")) != "P53"
        ):
            raise ValueError("Reference chain/entity correspondence requires review")
        if chain_ids != ["A", "B"] or chain_names != ["A", "B"]:
            raise ValueError("Unexpected label/author/native chain correspondence")
        receptor = list(
            msm.select(
                system, selection='chain_id=="A" and atom_type!="H" and atom_type!="D"'
            )
        )
        peptide = list(
            msm.select(
                system, selection='chain_id=="B" and atom_type!="H" and atom_type!="D"'
            )
        )
        fit = list(msm.select(system, selection='chain_id=="A" and atom_name=="CA"'))
        combined = list(receptor) + list(peptide)
        if (
            not receptor
            or not peptide
            or len(combined) > 2048
            or len(set(combined)) != len(combined)
        ):
            raise ValueError("Invalid or excessive observed-heavy-atom selections")
        original_coordinates = numeric(get(coordinates=True))
        if not np.isfinite(original_coordinates[:, combined]).all():
            raise ValueError("Nonfinite selected coordinates")
        if len(fit) < 3 or len(set(fit)) != len(fit):
            raise ValueError("Insufficient or repeated receptor-fit indices")
        # The public owner fit rejects collinearity before transforming any
        # structure; do not copy its geometric rank calculation downstream.
        maps = {}
        for attribute in (
            "atom_id",
            "atom_name",
            "atom_type",
            "group_index",
            "group_id",
            "group_name",
            "chain_index",
            "chain_id",
            "chain_name",
        ):
            maps[attribute] = np.asarray(get("atom", **{attribute: True})).tolist()
        if len(set(maps["atom_id"])) != len(maps["atom_id"]):
            raise ValueError("Ambiguous source atom identifiers")
        atom_rows_by_id = {row["id"]: row for row in atom_rows}
        if len(atom_rows_by_id) != len(atom_rows):
            raise ValueError("Duplicate source atom-site IDs")
        maps["source_atom_rows"] = [
            {
                key: atom_rows_by_id[atom_id][key]
                for key in (
                    "id",
                    "label_atom_id",
                    "auth_atom_id",
                    "label_asym_id",
                    "auth_asym_id",
                    "label_seq_id",
                    "auth_seq_id",
                    "pdbx_PDB_ins_code",
                    "label_alt_id",
                )
            }
            for atom_id in maps["atom_id"]
        ]
        maps.update(
            receptor_indices=list(map(int, receptor)),
            peptide_indices=list(map(int, peptide)),
            fit_indices=list(map(int, fit)),
            chain_ids=chain_ids,
            chain_names=chain_names,
        )
        write(directory / "atom-maps.json", maps)
        occupancies = np.asarray(get("atom", occupancy=True))
        alternates = get("atom", alternate_location=True)
        # This exact source is expected to have no alternate observations. A
        # nonempty owner object needs faithful native storage before proceeding.
        if alternates is not None and any(alternates):
            raise ValueError(
                "Nonempty alternate observations require native owner storage before geometry"
            )
        observations = {
            "structure_index": 0,
            "native_structure_id": np.asarray(get(structure_id=True)).tolist(),
            "source_model_identifier": source_models[0],
            "occupancy": np.where(np.isfinite(occupancies), occupancies, None).tolist(),
            "alternate_location": alternates,
            "connectivity_completeness": get(connectivity_completeness=True),
            "bond_evidence": list(get("bond", bond_evidence=True)),
            "chemistry": "source-declared or unassessed; no repair, hydrogen addition, force field or inferred-graph chemical-readiness claim",
        }
        write(directory / "observations.json", observations)
        admission = {
            "passed": True,
            "selected_atoms": len(combined),
            "receptor_atoms": len(receptor),
            "peptide_atoms": len(peptide),
            "fit_atoms": len(fit),
            "excluded_atoms": int(original_coordinates.shape[1] - len(combined)),
            "assembly": "deposited A/B pair; nonperiodic; no assembly/lattice transformation",
            "source": identity(source),
            "entry": "1YCR",
            "revision": [1, 5],
            "validation": "Retained report has independent provenance; exact coordinate-hash association not established",
        }
        views, arrays = {}, {}
        for name in ("reference", "rigid", "displaced"):
            view = msm.copy(system)
            if view is system:
                raise ValueError("Owner copy aliases the source object")
            if name == "rigid":
                msm.structure.rotate(
                    view,
                    rotation=np.array(
                        [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
                    ),
                    rotation_center=puw.quantity([0.0, 0.0, 0.0], "nm"),
                    selection=combined,
                    in_place=True,
                )
                msm.structure.translate(
                    view,
                    translation=puw.quantity([1.0, 2.0, 3.0], "nm"),
                    selection=combined,
                    in_place=True,
                )
            elif name == "displaced":
                msm.structure.translate(
                    view,
                    translation=puw.quantity([10.0, 0.0, 0.0], "nm"),
                    selection=peptide,
                    in_place=True,
                )
            msm.structure.least_rmsd_fit(
                view,
                selection=combined,
                selection_fit=fit,
                reference_molecular_system=system,
                reference_selection_fit=fit,
                in_place=True,
                use_gpu=False,
                precision="double",
                parallel=False,
                num_threads=1,
            )
            if name == "reference":
                admission["noncollinear_anchors_validated_by"] = (
                    "molsysmt.structure.least_rmsd_fit"
                )
                write(directory / "admission.json", admission)
            metrics = {}
            for label, selection in (("receptor", fit), ("peptide", peptide)):
                value = msm.structure.get_rmsd(
                    view,
                    selection=selection,
                    reference_molecular_system=system,
                    reference_selection=selection,
                    use_gpu=False,
                    parallel=False,
                    num_threads=1,
                )
                measured = numeric(value)
                if measured.size != 1 or not np.isfinite(measured).all():
                    raise ValueError("Unexpected fitted RMSD output")
                metrics[label + "_rmsd_nm"] = float(measured.item())
            views[name] = metrics
            distances = msm.structure.get_distances(
                view,
                selection=receptor,
                selection_2=peptide,
                pbc=False,
                use_gpu=False,
                parallel=False,
                num_threads=1,
            )
            arrays[name + "_distances"] = numeric(distances)
            for threshold in THRESHOLDS:
                suffix = f"{round(threshold * 100):03d}"
                arrays[name + "_contacts_" + suffix] = np.asarray(
                    msm.structure.get_contacts(
                        view,
                        selection=receptor,
                        selection_2=peptide,
                        threshold=puw.quantity(threshold, "nm"),
                        pbc=False,
                        use_gpu=False,
                        parallel=False,
                        num_threads=1,
                    )
                )
            if not np.array_equal(numeric(get(coordinates=True)), original_coordinates):
                raise ValueError("Reference coordinates changed through a derived view")
        checks = compare_views(views, arrays)
        arrays["reference_coordinates"] = original_coordinates
        for threshold in THRESHOLDS:
            arrays[f"boundary_pairs_{round(threshold * 100):03d}"] = (
                np.abs(arrays["reference_distances"] - threshold) <= TOLERANCE
            )
        np.savez_compressed(directory / "arrays.npz", **arrays)
        write(
            directory / "result.json",
            {
                "case": "MDM2-p53 T0",
                "entry": "1YCR",
                "revision": [1, 5],
                "views": views,
                "checks": checks,
                "passed": all(checks.values()),
                "arrays": {
                    key: {
                        "unit": "nm"
                        if "distances" in key or "coordinates" in key
                        else "dimensionless",
                        "shape": list(value.shape),
                        "dtype": str(value.dtype),
                    }
                    for key, value in arrays.items()
                },
                "array_file": identity(directory / "arrays.npz"),
                "thresholds": {
                    "value": list(THRESHOLDS),
                    "unit": "nm",
                    "primary": 0.45,
                },
                "tolerance": {"value": TOLERANCE, "unit": "nm"},
                "pbc": False,
                "interpretation": "Identity and artificial geometry controls only; no predictive recognition, affinity or biological utility evidence",
                "code": identity(__file__),
                "source": identity(source),
            },
        )
        return checks


def worker(task, directory):
    engine = supervision()
    engine.configure_child(
        {"cpu_ids": [0, 1], "address_space_bytes": 8 * 1024**3, "nice": 10},
        os.getppid(),
    )
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    os.environ.update(
        NUMBA_NUM_THREADS="1", RAYON_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1"
    )
    metadata_phase = True
    metadata_commands = []

    def offline(event, args):
        if (
            event == "subprocess.Popen"
            and metadata_phase
            and args[0] == "uname"
            and args[1] == ["uname", "-p"]
            and not metadata_commands
        ):
            executable = shutil.which("uname")
            if executable is None:
                raise RuntimeError("Planned uname metadata command is unavailable")
            metadata_commands.append(
                {"arguments": ["uname", "-p"], "executable": identity(executable)}
            )
            return
        if event in {
            "socket.connect",
            "socket.getaddrinfo",
            "subprocess.Popen",
            "os.system",
        }:
            raise RuntimeError(
                "T0 numerical worker forbids network and unplanned children"
            )

    sys.addaudithook(offline)
    declaration = json.loads((directory / "run-declaration.json").read_text())
    if identity(__file__) != declaration["code"]:
        raise ValueError("Worker code changed after declaration")
    log = (directory / "worker.log").open("x")
    os.dup2(log.fileno(), 1)
    os.dup2(log.fileno(), 2)
    try:
        import platform
        from importlib import metadata

        try:
            processor = platform.processor()
        finally:
            metadata_phase = False
        write(
            directory / "host-metadata.json",
            {
                "processor": processor,
                "planned_commands": metadata_commands,
                "new_geometry_operations": 0,
            },
        )

        profile_path = task / "profile-qualification.json"
        if identity(profile_path) != declaration["profile"]:
            raise ValueError("Qualified profile record changed after declaration")
        profile = json.loads(profile_path.read_text())
        versions = {}
        for distribution in metadata.distributions():
            versions.setdefault(distribution.metadata["Name"], distribution.version)
        if versions != profile["versions"]:
            raise ValueError(
                "Worker dependency inventory changed after profile receiving"
            )
        checks = geometry(task, directory)
        return 0 if all(checks.values()) else 1
    except Exception as exc:
        write(
            directory / "failure.json",
            {
                "type": type(exc).__name__,
                "message": str(exc),
                "traceback": traceback.format_exc(),
                "geometry_completed": False,
            },
        )
        return 1


def run(task):
    profile_path = task / "profile-qualification.json"
    profile = json.loads(profile_path.read_text())
    if profile.get("passed") is not True or profile.get("source_ref") != OWNER_REF:
        raise ValueError("Exact T0 application profile has not passed receiving")
    for pinned in profile["pinned_files"]:
        if identity(pinned["path"]) != pinned:
            raise ValueError("Qualified profile changed: " + pinned["path"])
    if profile["python"] != str(task / "clean-profile-stage/environment/bin/python"):
        raise ValueError("Unexpected isolated interpreter")
    directory = Path(tempfile.mkdtemp(prefix="geometry-", dir=task))
    command = [
        profile["python"],
        "-B",
        "-I",
        str(Path(__file__).resolve()),
        "_worker",
        "--task",
        str(task),
        "--directory",
        str(directory),
    ]
    write(
        directory / "run-declaration.json",
        {
            "authority": identity(
                ROOT / "devguide/evidence/mdm2_t0_authorization.json"
            ),
            "resource_authority": identity(
                ROOT / "devguide/evidence/mdm2_t0_resource_correction.json"
            ),
            "code": identity(__file__),
            "profile": identity(profile_path),
            "command": command,
            "limits": LIMITS,
            "planned_metadata_probe": {
                "public_api": "platform.processor",
                "maximum_uname_p_calls": 1,
                "scope": "stdlib/h5py cold-start host metadata only",
            },
            "supervision_code": identity(ROOT / "src/peptidemt/_hydramp_process.py"),
        },
    )
    facts = supervision().supervise(
        command, directory, SimpleNamespace(**LIMITS), include_supervisor_rss=True
    )
    drift = [
        pinned["path"]
        for pinned in profile["pinned_files"]
        if identity(pinned["path"]) != pinned
    ]
    if drift:
        facts["failure"] = "qualified_profile_changed_during_run"
        facts["changed_files"] = drift
    write(directory / "supervision.json", facts)
    print(json.dumps({"directory": str(directory), **facts}))
    return 0 if facts.get("returncode") == 0 and facts.get("failure") is None else 1


def inspect(directory):
    """Inspect saved outputs without importing molecular/numerical providers."""
    result = json.loads((directory / "result.json").read_text())
    if (
        result.get("case") != "MDM2-p53 T0"
        or result.get("entry") != "1YCR"
        or result.get("revision") != [1, 5]
        or result.get("pbc") is not False
        or result["thresholds"]
        != {"value": list(THRESHOLDS), "unit": "nm", "primary": 0.45}
        or result["tolerance"] != {"value": TOLERANCE, "unit": "nm"}
        or not result["checks"]
        or not all(type(value) is bool for value in result["checks"].values())
        or result["passed"] is not all(result["checks"].values())
    ):
        raise ValueError("Saved result does not retain the fixed T0 definitions")
    if identity(directory / "arrays.npz") != result["array_file"]:
        raise ValueError("Saved array artifact changed")
    if result["thresholds"]["unit"] != "nm" or result["tolerance"]["unit"] != "nm":
        raise ValueError("Unexpected saved quantity unit")
    for key, value in result["arrays"].items():
        expected = (
            "nm" if "distances" in key or "coordinates" in key else "dimensionless"
        )
        if value["unit"] != expected:
            raise ValueError("Unexpected saved array unit: " + key)
    return {
        "passed": result["passed"],
        "checks": result["checks"],
        "saved_array_sha256": result["array_file"]["sha256"],
        "new_geometry_operations": 0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("acquire", "run", "inspect", "_worker"))
    parser.add_argument("--task", type=Path, required=True)
    parser.add_argument("--directory", type=Path)
    args = parser.parse_args()
    task = args.task.resolve()
    if args.operation == "acquire":
        print(json.dumps(acquire(task), indent=2))
    elif args.operation == "run":
        return run(task)
    elif args.operation == "_worker":
        return worker(task, args.directory.resolve())
    else:
        print(json.dumps(inspect(args.directory.resolve()), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
