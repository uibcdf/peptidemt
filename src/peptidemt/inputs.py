"""Ordered peptide proposals and sequence-preserving increment-1 admission."""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path

from ._data import mapping

_ALPHABET = frozenset("ACDEFGHIKLMNPQRSTVWY")


@dataclass(frozen=True)
class SequenceRecord:
    """A supplied proposal, with unresolved chemistry left unresolved.

    ``None`` denotes an incomplete sequence; ``""`` denotes an empty sequence.
    Chemical annotations are retained, but this first sequence-only route cannot
    qualify or project an explicitly annotated chemical realization.
    """

    sequence: str | None
    header: str | None = None
    chemistry: Mapping = field(default_factory=dict)
    context: Mapping = field(default_factory=dict)
    source: str | None = None
    raw_record: str | None = None

    def __post_init__(self):
        for name in ("sequence", "header", "source", "raw_record"):
            value = getattr(self, name)
            if value is not None and not isinstance(value, str):
                raise TypeError(f"{name} must be a string or None")
        for name in ("chemistry", "context"):
            object.__setattr__(self, name, mapping(getattr(self, name)))


@dataclass(frozen=True)
class InputRecord:
    """Run-local correspondence, not molecular identity."""

    occurrence: int
    proposal: SequenceRecord

    def __post_init__(self):
        if type(self.occurrence) is not int or self.occurrence < 0:
            raise ValueError("occurrence must be a nonnegative integer")
        if not isinstance(self.proposal, SequenceRecord):
            raise TypeError("proposal must be a SequenceRecord")

    @property
    def token(self) -> str:
        return f"input-{self.occurrence}"

    @property
    def issues(self) -> tuple[str, ...]:
        """Operation-specific incompatibilities; never alter the original."""
        sequence = self.proposal.sequence
        reasons = []
        if sequence is None:
            reasons.append("incomplete_sequence")
        elif not sequence:
            reasons.append("empty_sequence")
        else:
            if not set(sequence) <= _ALPHABET:
                reasons.append("unsupported_symbols")
            if sequence.startswith("M"):
                reasons.append("sequence_changing_native_preprocessing")
            if len(sequence) >= 100:
                reasons.append("outside_provisional_length_scope")
        if self.proposal.chemistry:
            reasons.append("unassessed_explicit_chemistry")
        return tuple(reasons)

    @property
    def provider_sequence(self) -> str | None:
        return None if self.issues else self.proposal.sequence


def prepare_sequences(
    records: Iterable[str | SequenceRecord],
) -> tuple[InputRecord, ...]:
    """Keep every occurrence, including empty, repeated and incompatible proposals."""
    if isinstance(records, (str, bytes, Mapping)):
        raise TypeError(
            "records must be an iterable of sequence records, not one string"
        )
    prepared = []
    for index, record in enumerate(records):
        if isinstance(record, str):
            record = SequenceRecord(record)
        if not isinstance(record, SequenceRecord):
            raise TypeError("Each record must be a string or SequenceRecord")
        prepared.append(InputRecord(index, record))
    return tuple(prepared)


def parse_fasta(text: str, *, source: str | None = None) -> tuple[SequenceRecord, ...]:
    """Join sequence lines, retaining full headers and verbatim record text.

    Only line terminators are removed from sequence lines. Whitespace, lowercase,
    stops and modification syntax are not silently repaired. Nonblank content
    before a header raises ValueError rather than losing an unnamed proposal.
    """
    if not isinstance(text, str):
        raise TypeError("FASTA input must be text")
    records = []
    header = None
    lines = []
    raw = []
    for number, line in enumerate(text.splitlines(keepends=True), start=1):
        content = line.removesuffix("\n").removesuffix("\r")
        if content.startswith(">"):
            if header is not None:
                records.append(
                    SequenceRecord(
                        "".join(lines), header, source=source, raw_record="".join(raw)
                    )
                )
            header, lines, raw = content[1:], [], [line]
        elif header is None:
            if content.strip():
                raise ValueError(f"FASTA sequence before first header at line {number}")
        else:
            lines.append(content)
            raw.append(line)
    if header is not None:
        records.append(
            SequenceRecord(
                "".join(lines), header, source=source, raw_record="".join(raw)
            )
        )
    return tuple(records)


def read_fasta(path: str | Path) -> tuple[SequenceRecord, ...]:
    """Read UTF-8 FASTA without newline translation; retain the source path."""
    with Path(path).open(encoding="utf-8", newline="") as stream:
        return parse_fasta(stream.read(), source=str(path))
