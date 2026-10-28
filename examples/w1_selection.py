"""Replay the explicitly invented D35 fixture. No scientific provider executes."""

from peptidemt import Provenance, ProviderRow, ResultSet, prepare_sequences, select


def main():
    inputs = prepare_sequences(["ACD"] * 5)
    rows = []
    for item, (amp, hemo) in zip(
        inputs,
        ((0.9, 0.8), (0.4, 0.1), (0.9, 0.2), (0.9, 0.2), (0.95, None)),
        strict=True,
    ):
        values = {
            "Sequence": item.proposal.sequence,
            "AMP_probability": amp,
            "is_AMP": amp > 0.5,
            "AMP_family": "ALP",
        }
        if hemo is not None:
            values.update(
                Hemolytic_probability=hemo,
                Hemolytic="Hemo" if hemo > 0.5 else "NonHemo",
            )
        rows.append(ProviderRow(item.token, values))
    snapshot = ResultSet(
        snapshot_id="D35-invented-fixture",
        inputs=inputs,
        rows=tuple(rows),
        provenance=Provenance(
            provider="invented-fixture",
            bundle_id="D35-toy-values",
            evidence_kind="controlled-fixture",
            details={"provider_executed": False, "scientific_data": False},
        ),
    )
    replay = ResultSet.from_json(snapshot.to_json())
    for policy in ("amp-first", "hemolysis-first"):
        choice = select(replay, policy=policy, k=2)
        expected = (
            ("input-2", "input-3") if policy == "amp-first" else ("input-1", "input-2")
        )
        assert choice.selected == expected
        assert choice.excluded[0][0] == "input-4"
        print(policy, "selected:", choice.selected, "excluded:", choice.excluded)


if __name__ == "__main__":
    main()
