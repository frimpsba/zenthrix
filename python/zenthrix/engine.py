"""Public inference API and private-engine integration boundary."""

from dataclasses import dataclass
from math import isfinite
from pathlib import Path

from .exceptions import EngineUnavailableError
from .validation import validate_compiled_model_path


@dataclass(frozen=True, slots=True)
class InferenceResult:
    """Result returned by a provisioned native runtime."""

    text: str
    ttft_ms: float
    tokens_per_second: float


class Engine:
    """Handle a compiled model through the optional native engine.

    The native engine is distributed separately from this public package. The
    frontend validates the model path and reports a clear installation error
    until that engine is provisioned.
    """

    def __init__(self, model_path: str | Path) -> None:
        self.model_path = validate_compiled_model_path(model_path)

    def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.2,
        max_tokens: int = 256,
    ) -> InferenceResult:
        """Generate text using the optional native engine."""
        if not prompt.strip():
            raise ValueError("prompt must not be empty")
        if not isfinite(temperature) or temperature < 0:
            raise ValueError("temperature must be a finite non-negative number")
        if max_tokens < 1:
            raise ValueError("max_tokens must be at least 1")
        raise EngineUnavailableError(
            "The Zenthrix native engine is not installed. "
            "Install the platform runtime before calling Engine.generate()."
        )
