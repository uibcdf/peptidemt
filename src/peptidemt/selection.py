"""The two D35 lexicographic occurrence selectors on unchanged evidence."""

from dataclasses import dataclass

from .results import Provenance, ResultSet


@dataclass(frozen=True)
class Selection:
    snapshot_id: str
    provenance: Provenance
    policy: str
    requested_count: int
    ranking: tuple[str, ...]
    selected: tuple[str, ...]
    unselected: tuple[str, ...]
    excluded: tuple[tuple[str, tuple[str, ...]], ...]
    tie_rule: str = "earlier original input occurrence"


def select(results: ResultSet, *, policy: str, k: int) -> Selection:
    """Rank eligible occurrences; a computational preference, not activity/safety.

    ``amp-first``: AMP descending, hemolysis ascending, original occurrence.
    ``hemolysis-first``: hemolysis ascending, AMP descending, same final tie rule.
    No native-label gate, deduplication, rounding or missing-score imputation.
    """
    if not isinstance(results, ResultSet):
        raise TypeError("results must be a ResultSet")
    if policy not in ("amp-first", "hemolysis-first"):
        raise ValueError("policy must be 'amp-first' or 'hemolysis-first'")
    if type(k) is not int:
        raise TypeError("k must be an integer, not bool or a coerced number")
    if k < 0:
        raise ValueError("k must be nonnegative")
    eligible, excluded = [], []
    for occurrence, outcome in enumerate(results.outcomes):
        if outcome.issues:
            excluded.append((outcome.token, outcome.issues))
            continue
        values = results.rows[outcome.row_index].values
        amp, hemo = values["AMP_probability"], values["Hemolytic_probability"]
        key = (
            (-amp, hemo, occurrence)
            if policy == "amp-first"
            else (hemo, -amp, occurrence)
        )
        eligible.append((key, outcome.token))
    ranking = tuple(token for _, token in sorted(eligible))
    return Selection(
        results.snapshot_id,
        results.provenance,
        policy,
        k,
        ranking,
        ranking[:k],
        ranking[k:],
        tuple(excluded),
    )
