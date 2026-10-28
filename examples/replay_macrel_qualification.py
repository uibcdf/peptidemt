"""Replay the real, bounded W3 snapshot without importing its scientific engine.

Run this example from the source repository using an installed PeptideMT.
The saved fixture supports computational selection, not biological acceptance.
"""

import sys
from pathlib import Path

from peptidemt import ResultSet, select


def main():
    path = (
        Path(__file__).resolve().parents[1]
        / "devguide/evidence/w3_native/qualified-computational.json"
    )
    results = ResultSet.from_json(path.read_text(encoding="utf-8"))
    amp = select(results, policy="amp-first", k=3)
    hemo = select(results, policy="hemolysis-first", k=3)
    assert amp.selected == ("input-0", "input-4", "input-2")
    assert hemo.selected == ("input-1", "input-3", "input-2")
    assert len(results.inputs) == 17 and len(results.rows) == 6
    assert (
        results.provenance.details["scientific_attribution"]["producer"]["version"]
        == "0.1.0+95.g7a299d1"
    )
    assert "macrel" not in sys.modules and "ackredit" not in sys.modules
    print("amp-first:", amp.selected)
    print("hemolysis-first:", hemo.selected)
    print(
        "Original producer, exact native values and bibliography preserved; no new calculation."
    )


if __name__ == "__main__":
    main()
