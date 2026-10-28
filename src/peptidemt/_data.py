"""Immutable, detached result data and lossless JSON encoding (no engine imports)."""

from collections.abc import Mapping
from types import MappingProxyType


def freeze(value):
    """Detach supported data from caller-owned containers without coercing values."""
    if value is None or type(value) in (str, bool, int, float):
        return value
    if isinstance(value, Mapping):
        if any(type(key) is not str for key in value):
            raise TypeError("Data mapping keys must be strings")
        return MappingProxyType({key: freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(freeze(item) for item in value)
    raise TypeError(f"Unsupported result data type: {type(value).__name__}")


def mapping(value):
    if not isinstance(value, Mapping):
        raise TypeError("Expected a data mapping")
    return freeze(value)


def nonempty_text(value, name):
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")
    if not value:
        raise ValueError(f"{name} must not be empty")
    return value


def encode(value):
    # Tag every mapping, so user keys cannot collide with the float tag.
    if isinstance(value, Mapping):
        return {"mapping": {key: encode(item) for key, item in value.items()}}
    if isinstance(value, tuple):
        return [encode(item) for item in value]
    if type(value) is float:
        return {"float_hex": value.hex()}
    return value


def decode(value):
    if isinstance(value, dict):
        if set(value) == {"mapping"} and isinstance(value["mapping"], dict):
            return {key: decode(item) for key, item in value["mapping"].items()}
        if set(value) == {"float_hex"} and isinstance(value["float_hex"], str):
            return float.fromhex(value["float_hex"])
        raise ValueError("Invalid tagged result data")
    if isinstance(value, list):
        return tuple(decode(item) for item in value)
    if value is None or type(value) in (str, bool, int):
        return value
    raise ValueError("Untagged floating-point or unsupported result data")
