"""Actual owner-backed ingestion and its consumer boundary; no model runs."""

import subprocess
import sys
from types import SimpleNamespace

import pytest

from peptidemt import parse_fasta, prepare_sequences, read_fasta
from peptidemt._diagnostics import RequiredDependencyError


@pytest.mark.parametrize("ending", ["\n", "\r\n", "\r"])
def test_actual_owner_preserves_input_and_occurrence_correspondence(tmp_path, ending):
    text = ending + ending.join(
        [">full header  ", " acD ", "A*", ">repeat", "MACD", ">repeat", "MACD", ">", ""]
    )
    path = tmp_path / "submitted.fasta"
    path.write_bytes(text.encode())
    records = read_fasta(path)
    assert records == parse_fasta(text, source=str(path))
    assert [r.header for r in records] == ["full header  ", "repeat", "repeat", ""]
    assert [r.sequence for r in records] == [" acD A*", "MACD", "MACD", ""]
    assert ending + "".join(r.raw_record for r in records) == text
    assert path.read_bytes() == text.encode()
    inputs = prepare_sequences(records)
    assert [i.token for i in inputs] == ["input-0", "input-1", "input-2", "input-3"]
    assert [i.issues for i in inputs] == [
        ("unsupported_symbols",),
        ("sequence_changing_native_preprocessing",),
        ("sequence_changing_native_preprocessing",),
        ("empty_sequence",),
    ]


def test_unicode_separators_remain_unassessed_sequence_content():
    text = ">raw\nAC\u2028>still-sequence\n"
    records = parse_fasta(text)
    assert len(records) == 1
    assert records[0].raw_record == text
    assert records[0].sequence == "AC\u2028>still-sequence"
    assert prepare_sequences(records)[0].issues == ("unsupported_symbols",)


def test_wrappers_use_the_public_owner_for_text_and_file(monkeypatch):
    from peptidemt import _molsysmt as boundary

    calls = []

    def owner(*args, **kwargs):
        calls.append((args, kwargs))
        return {
            "schema": "molsysmt.fasta_source@1",
            "source": "owner-source",
            "preamble": "",
            "records": [
                {"sequence": "ACD", "header": "full", "raw_record": "owner-raw"}
            ],
        }

    monkeypatch.setattr(
        boundary,
        "_load_molsysmt",
        lambda: SimpleNamespace(
            form=SimpleNamespace(
                file_fasta=SimpleNamespace(parse_records=owner, read_records=owner)
            )
        ),
    )
    # Deliberately not FASTA: the consumer must not interpret the owner's input.
    parsed = parse_fasta("opaque text", source="submitted")
    received = read_fasta("opaque.fasta")
    assert parsed == received
    assert parsed[0].source == "owner-source" and parsed[0].raw_record == "owner-raw"
    assert calls == [
        (("opaque text",), {"source_label": "submitted"}),
        (("opaque.fasta",), {}),
    ]


@pytest.mark.parametrize("text", ["ACD\n>a\nG", "\ufeff>a\nACD", " >a\nACD"])
def test_format_errors_preserve_owner_diagnostic_as_cause(text):
    from smonitor.integrations import FormatError

    with pytest.raises(ValueError, match="before the first header") as caught:
        parse_fasta(text)
    assert isinstance(caught.value.__cause__, FormatError)
    assert caught.value.__cause__.code == "MSM-ERR-IO-003"


def test_file_errors_and_original_source_label(tmp_path):
    from smonitor.integrations import FormatError

    with pytest.raises(FileNotFoundError):
        read_fasta(tmp_path / "missing.fa")
    invalid = tmp_path / "invalid.fa"
    invalid.write_bytes(b">a\n\xff\n")
    with pytest.raises(UnicodeDecodeError) as caught:
        read_fasta(invalid)
    assert isinstance(caught.value.__cause__, FormatError)
    assert caught.value.object == b">a\n\xff\n"
    assert invalid.read_bytes() == b">a\n\xff\n"
    # File suffix validation belongs to the owner, with no local bypass.
    import molsysmt

    with pytest.raises(molsysmt.ArgumentError):
        read_fasta(tmp_path / "not-a-fasta.txt")


@pytest.mark.parametrize("call", [lambda: parse_fasta(None), lambda: read_fasta(3)])
def test_invalid_argument_types_are_explicit(call):
    with pytest.raises(TypeError):
        call()


def test_absence_is_guarded_without_invented_installers(monkeypatch):
    from depdigest.core import checker

    checker.is_installed.cache_clear()
    monkeypatch.setattr(checker, "find_spec", lambda name: None)
    try:
        for call in (lambda: parse_fasta(">a\nACD"), lambda: read_fasta("a.fa")):
            with pytest.raises(RequiredDependencyError) as caught:
                call()
            message = str(caught.value)
            assert "molsysmt" in message and "Macrel" not in message
            assert "pip install" not in message and "conda install" not in message
    finally:
        checker.is_installed.cache_clear()


def test_broken_installed_provider_is_not_reported_as_absent(monkeypatch):
    from depdigest.core import checker

    checker.is_installed.cache_clear()
    monkeypatch.setattr(checker, "find_spec", lambda name: SimpleNamespace())
    monkeypatch.setitem(sys.modules, "molsysmt", None)
    try:
        with pytest.raises(ModuleNotFoundError):
            parse_fasta(">a\nACD")
    finally:
        checker.is_installed.cache_clear()


def test_memory_inputs_and_saved_replay_need_no_molecular_or_model_provider():
    script = """
import sys
from importlib.abc import MetaPathFinder
class DenyProviders(MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] in {'molsysmt','macrel','Bio','onnxruntime','ackredit'}:
            raise AssertionError('Unexpected provider import: ' + fullname)
sys.meta_path.insert(0, DenyProviders())
from peptidemt import Provenance, ResultSet, prepare_sequences, select
inputs = prepare_sequences(['ACD','ACD',''])
saved = ResultSet(snapshot_id='engine-absent',inputs=inputs,rows=(),
    provenance=Provenance(provider='none',bundle_id='none',evidence_kind='controlled-fixture'))
restored = ResultSet.from_json(saved.to_json())
assert restored.inputs == inputs
for policy in ('amp-first','hemolysis-first'):
    assert select(restored,policy=policy,k=0).selected == ()
assert 'molsysmt' not in sys.modules and 'macrel' not in sys.modules
"""
    subprocess.run([sys.executable, "-I", "-c", script], check=True)
