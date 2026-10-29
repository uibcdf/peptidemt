"""Ingest actual owner-backed FASTA; no scientific evaluator is invoked."""

import sys

from peptidemt import parse_fasta, prepare_sequences


def main():
    text = ">full repeated header\r\nAC\r\nD\r\n>full repeated header\nACD\n>empty\n"
    records = parse_fasta(text, source="example-text")
    inputs = prepare_sequences(records)
    assert [r.sequence for r in records] == ["ACD", "ACD", ""]
    assert "".join(r.raw_record for r in records) == text
    assert [i.token for i in inputs] == ["input-0", "input-1", "input-2"]
    assert inputs[2].issues == ("empty_sequence",)
    assert "macrel" not in sys.modules and "onnxruntime" not in sys.modules
    print("MolSysMT FASTA ingestion: three preserved occurrences, no model execution")


if __name__ == "__main__":
    main()
