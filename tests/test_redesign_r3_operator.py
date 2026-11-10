"""Finite execution authority and one-attempt guards; no scientific engines."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "redesign_r3_operator", ROOT / "devtools/hydramp_redesign_r3.py"
)
driver = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(driver)


def test_absent_approval_cannot_start_or_create_a_run(tmp_path):
    with pytest.raises(FileNotFoundError):
        driver.execute(tmp_path, {})
    assert not (tmp_path / "run").exists()


@pytest.mark.parametrize("approval", [{}, {"explicit_investigator_approval": True}])
def test_incomplete_approval_cannot_open_a_scientific_run(tmp_path, approval):
    (tmp_path / "authorization.json").write_text(json.dumps(approval))
    (tmp_path / "plan.json").write_text("{}")
    with pytest.raises(ValueError, match="authorization"):
        driver.execute(tmp_path, {})
    assert not (tmp_path / "run").exists()


def test_changed_pin_is_rejected_before_model_loading(tmp_path):
    artifact = tmp_path / "artifact"
    artifact.write_text("changed")
    with pytest.raises(ValueError, match="Changed pinned file"):
        driver.verify({"pins": [{"path": str(artifact), "sha256": "0" * 64}]})


def test_added_distribution_is_rejected_before_model_loading(tmp_path):
    consumer = tmp_path / "site/peptidemt"
    consumer.mkdir(parents=True)
    metadata = tmp_path / "site/unexpected-1.dist-info"
    metadata.mkdir()
    (metadata / "METADATA").write_text("Name: unexpected\nVersion: 1\n")
    with pytest.raises(ValueError, match="Changed installed profile inventory"):
        driver.verify(
            {
                "pins": [],
                "consumer_source": {},
                "profiles": {"test": {"consumer_root": str(consumer), "inventory": {}}},
            }
        )


@pytest.mark.parametrize("failure", [None, "timeout", "resident_memory_guard"])
def test_fixed_dispatch_order_and_consumed_failure_slot(tmp_path, monkeypatch, failure):
    import peptidemt._hydramp_process as process

    calls = []
    monkeypatch.setattr(driver, "authorize", lambda task, plan: None)

    def supervised(command, directory, limits):
        calls.append((command[0], directory.name))
        return {
            "started": True,
            "returncode": 0 if failure is None else -9,
            "failure": failure,
        }

    monkeypatch.setattr(process, "supervise", supervised)
    plan = {
        "profiles": {
            "generation": {"python": "generator"},
            "assessment": {"python": "assessor"},
        },
        "supervisor_limits": {},
    }
    if failure:
        with pytest.raises(RuntimeError, match="R3 stopped"):
            driver.execute(tmp_path, plan)
        assert calls == [("generator", "direct")]
        assert not (tmp_path / "run/adapter").exists()
    else:
        driver.execute(tmp_path, plan)
        assert calls == [("generator", "direct")] + [
            ("assessor", name)
            for name in ("adapter", "repeat", "controls", "parents", "children")
        ]
    with pytest.raises(FileExistsError):
        driver.execute(tmp_path, plan)
    assert len(calls) == (1 if failure else 6)
