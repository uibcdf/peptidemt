"""Authorization/budget controls only; no model is ever imported."""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

import peptidemt

spec = importlib.util.spec_from_file_location(
    "hydramp_execution_qualification_test",
    Path(__file__).parents[1] / "hydramp_execution_qualification.py",
)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


def test_absent_or_other_plan_approval_blocks_before_importing_scientific_route(
    tmp_path,
):
    plan = {"work_dir": str(tmp_path)}
    with pytest.raises(FileNotFoundError):
        tool.case(plan, "not-approved")
    (tmp_path / "authorization.json").write_text(
        json.dumps(
            {"plan_sha256": "other", "investigator_reference": "artificial control"}
        )
    )
    with pytest.raises(ValueError, match="approval"):
        tool.case(plan, "not-approved")


def test_expanded_budget_is_rejected_before_reading_any_artifact():
    plan = {
        "schema": "peptidemt.hydramp_execution_adapter_plan@1",
        "request": {
            "n_target": 16,
            "seed": 1001,
            "snapshot_id": "installed-HydrAMP-seed-1001",
            "qualification_reference": None,
        },
        "call_budget": {"public_generation_calls": 2},
    }
    with pytest.raises(ValueError, match="budget"):
        tool.preflight(plan)


@pytest.mark.skipif(sys.platform != "linux", reason="Linux process resource contract")
def test_parent_soft_limit_preserves_inherited_worker_hard_ceiling(tmp_path):
    # Tiny stdlib processes set virtual ceilings without allocating those bytes.
    program = """
import sys,json,os,resource,subprocess,importlib.util
from pathlib import Path
sys.path.insert(0,sys.argv[2])
spec=importlib.util.spec_from_file_location('qualification_control',sys.argv[1])
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
plan={'limits':{'address_space_bytes':8*1024**3,'cpu_ids':list(os.sched_getaffinity(0)),'nice':10},
      'resources':{'parent_address_space_bytes':1024**3}}
module.configure_parent(plan)
assert resource.getrlimit(resource.RLIMIT_AS)==(1024**3,8*1024**3)
child='import resource,json;resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,)*2);print(json.dumps(resource.getrlimit(resource.RLIMIT_AS)))'
data=json.loads(subprocess.check_output([sys.executable,'-B','-I','-c',child],text=True))
assert data==[8*1024**3,8*1024**3]
print('parent soft1GiB/hard8GiB;worker can set8GiB;no scientific imports')
"""
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            "-I",
            "-c",
            program,
            str(Path(tool.__file__)),
            str(Path(peptidemt.__file__).parent.parent),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        start_new_session=True,
        timeout=10,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_failed_scientific_case_never_reports_success_from_clean_process_exit():
    assert tool.exit_code({"completed": False, "failures": ["worker_preflight"]}) == 1
    assert tool.exit_code({"failure": "worker_failure", "returncode": 1}) == 1
    assert tool.exit_code({"files_hashed": 1}) == 0
