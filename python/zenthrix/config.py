"""Configuration types shared by the CLI and Python API."""

from dataclasses import dataclass

SUPPORTED_TARGETS = frozenset({"apple", "arm", "auto", "qualcomm"})
SUPPORTED_QUANTIZATIONS = frozenset({"fp16", "int4", "int8"})


@dataclass(frozen=True, slots=True)
class CompileConfig:
    """Options describing a compilation request."""

    target: str = "auto"
    quantization: str | None = None
