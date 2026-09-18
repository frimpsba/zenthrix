"""GGUF input validation."""

from pathlib import Path

from ..validation import validate_model_path


def validate_gguf(path: str | Path) -> Path:
    """Validate a GGUF model path."""
    model_path = validate_model_path(path)
    if model_path.suffix.lower() != ".gguf":
        raise ValueError(f"Expected a .gguf file, got: {model_path}")
    return model_path

