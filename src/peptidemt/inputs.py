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
    """Receive source-preserving records from MolSysMT's public FASTA reader.

    Requires the development-source ``file_fasta.parse_records`` capability.
    Only CR/LF line terminators are removed from sequence lines. Other characters,
    full headers, repeated and empty occurrences remain unchanged. Provider format
    errors become ValueError with their original cause; no local parser is used.
    """
    if not isinstance(text, str):
        raise TypeError("FASTA input must be text")
    if source is not None and not isinstance(source, str):
        raise TypeError("source must be a string or None")
    from ._molsysmt import _load_molsysmt

    reader = _load_molsysmt().form.file_fasta.parse_records
    return _receive_fasta(reader, text, source_label=source)


def read_fasta(path: str | Path) -> tuple[SequenceRecord, ...]:
    """Delegate strict UTF-8 file reading to MolSysMT, retaining the source path.

    Paths follow the owner's public FASTA form contract (``.fa`` or ``.fasta``).
    Newlines are untranslated. Decoding failures remain UnicodeDecodeError with
    the provider error as cause; other I/O errors propagate unchanged.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError("FASTA path must be a string or Path")
    from ._molsysmt import _load_molsysmt

    reader = _load_molsysmt().form.file_fasta.read_records
    return _receive_fasta(reader, path)


def _receive_fasta(reader, *args, **kwargs):
    """Adapt owner records to peptide proposals without interpreting FASTA."""
    from smonitor.integrations import FormatError

    try:
        document = reader(*args, **kwargs)
    except FormatError as error:
        cause = error.__cause__
        if isinstance(cause, UnicodeDecodeError):
            raise UnicodeDecodeError(
                cause.encoding, cause.object, cause.start, cause.end, cause.reason
            ) from error
        raise ValueError(str(error)) from error
    if document["schema"] != "molsysmt.fasta_source@1":
        raise ValueError("Unsupported MolSysMT FASTA source schema")
    return tuple(
        SequenceRecord(
            record["sequence"],
            header=record["header"],
            source=document["source"],
            raw_record=record["raw_record"],
        )
        for record in document["records"]
    )
