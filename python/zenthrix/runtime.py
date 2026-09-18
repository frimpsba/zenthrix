"""Runtime adapter boundary for the separately distributed native engine."""

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .exceptions import EngineUnavailableError


class RuntimeAdapter(Protocol):
    """Operations supplied by an installed native runtime."""

    def generate(
        self,
        model_path: Path,
        prompt: str,
        *,
        temperature: float,
        max_tokens: int,
    ) -> "RuntimeResult":
        """Generate text for a compiled model."""


@dataclass(frozen=True, slots=True)
class RuntimeResult:
    """Runtime-neutral inference result."""

    text: str
    ttft_ms: float
    tokens_per_second: float


class UnavailableRuntime:
    """Runtime implementation used when the native engine is not provisioned."""

    def generate(
        self,
        model_path: Path,
        prompt: str,
        *,
        temperature: float,
        max_tokens: int,
    ) -> RuntimeResult:
        del model_path, prompt, temperature, max_tokens
        raise EngineUnavailableError(
            "The Zenthrix native engine is not installed. "
            "Install the platform runtime before calling inference."
        )


def default_runtime() -> RuntimeAdapter:
    """Return the provisioned runtime or an explicit unavailable boundary."""
    return UnavailableRuntime()
