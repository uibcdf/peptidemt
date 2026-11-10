"""Declared artificial native trace; not generated or biological evidence."""

from peptidemt import (
    HydrAMPAnalogueReceipt,
    Provenance,
    SequenceRecord,
    prepare_sequences,
)


def artificial_receipt():
    parents = prepare_sequences(
        [
            SequenceRecord("ACD", header="first", context={"measured": "parent only"}),
            SequenceRecord(None),
            SequenceRecord("ACD", header="repeat"),
            SequenceRecord("MAA"),
            SequenceRecord("ACD", chemistry={"terminal": "explicit"}),
        ]
    )

    def pad(row):
        return row + [0] * (25 - len(row))

    protos = [pad([1, 2, 3]), pad([1, 2, 3]), pad([11, 1, 1])]
    tokens = [
        pad(row)
        for row in (
            [9, 1, 1, 1, 1],
            [9, 1, 1, 1, 1],
            [11, 1, 1, 1, 1],
            [9, 1, 1, 1, 1],
            [10, 1, 1, 1, 1],
            [11, 1, 1],
            [],
            [1, 2, 3],
            [13, 1, 1, 1, 1],
        )
    ]
    t = dict(
        seed=7,
        temperature=1.0,
        n_attempts=3,
        prototype_tokens=protos,
        prototype_mean=[[0.0] * 64 for _ in range(3)],
        prototype_log_variance=[[0.0] * 64 for _ in range(3)],
        prototype_std=[[1.0] * 64 for _ in range(3)],
        prototype_scale=[[1.0] * 64 for _ in range(3)],
        std_underflow=[[False] * 64 for _ in range(3)],
        scale_underflow=[[False] * 64 for _ in range(3)],
        prototype_amp=[0.3] * 3,
        prototype_mic=[0.2] * 3,
        prototype_indices=[0, 1, 2] * 3,
        attempt_indices=[0] * 3 + [1] * 3 + [2] * 3,
        submitted_tokens=protos * 3,
        means=[[0.0] * 64 for _ in range(9)],
        noise=[[0.0] * 64 for _ in range(9)],
        latents=[[0.0] * 64 for _ in range(9)],
        conditioned=[[0.0] * 64 + [1.0, 1.0] for _ in range(9)],
        decoder_inputs=[[0.0] * 64 + [1.0, 1.0] for _ in range(9)],
        tokens=tokens,
        sequences=[
            "KAAAA",
            "KAAAA",
            "MAAAA",
            "KAAAA",
            "LAAAA",
            "MAA",
            "",
            "ACD",
            "PAAAA",
        ],
        amp=[0.8] * 8 + [0.2],
        mic=[0.7] * 9,
        improves=[True] * 8 + [False],
        excludes_self=[False] * 5 + [True, False, True, False],
        projected_empty=[False] * 6 + [True, False, False],
        duplicate=[False, False, False, True, False, False, False, False, False],
        retained=[True, True, True, False, True, False, True, False, False],
        results=[
            {
                "prototype_index": 0,
                "prototype_sequence": "ACD",
                "amp": 0.3,
                "mic": 0.2,
                "candidates": [
                    {
                        "sequence": "",
                        "trace_row": 6,
                        "attempt_index": 2,
                        "amp": 0.8,
                        "mic": 0.7,
                    },
                    {
                        "sequence": "KAAAA",
                        "trace_row": 0,
                        "attempt_index": 0,
                        "amp": 0.8,
                        "mic": 0.7,
                    },
                ],
            },
            {
                "prototype_index": 1,
                "prototype_sequence": "ACD",
                "amp": 0.3,
                "mic": 0.2,
                "candidates": [
                    {
                        "sequence": "KAAAA",
                        "trace_row": 1,
                        "attempt_index": 0,
                        "amp": 0.8,
                        "mic": 0.7,
                    },
                    {
                        "sequence": "LAAAA",
                        "trace_row": 4,
                        "attempt_index": 1,
                        "amp": 0.8,
                        "mic": 0.7,
                    },
                ],
            },
            {
                "prototype_index": 2,
                "prototype_sequence": "MAA",
                "amp": 0.3,
                "mic": 0.2,
                "candidates": [
                    {
                        "sequence": "MAAAA",
                        "trace_row": 2,
                        "attempt_index": 0,
                        "amp": 0.8,
                        "mic": 0.7,
                    }
                ],
            },
        ],
    )
    return HydrAMPAnalogueReceipt(
        "controlled",
        parents,
        7,
        1.0,
        3,
        (0, 2, 3),
        Provenance("invented-analogue", "synthetic", "controlled-fixture"),
        t,
    )
