"""Configuration types shared by the CLI and Python API."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CompileConfig:
    """Options describing a compilation request."""

    target: str = "auto"
    quantization: str | None = None

