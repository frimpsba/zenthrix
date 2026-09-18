"""Validation helpers for model inputs and compiler options."""

from pathlib import Path

from .exceptions import InputValidationError

SUPPORTED_FORMATS = frozenset({"onnx", "pytorch", "gguf"})


def validate_model_path(path: str | Path) -> Path:
    """Return an existing regular model path or raise a useful error."""
    model_path = Path(path)
    if not model_path.exists():
        raise InputValidationError(f"Model path does not exist: {model_path}")
    if not model_path.is_file():
        raise InputValidationError(f"Model path is not a file: {model_path}")
    return model_path


def validate_model_format(model_format: str) -> str:
    """Normalize and validate a supported model format."""
    normalized = model_format.lower()
    if normalized not in SUPPORTED_FORMATS:
        supported = ", ".join(sorted(SUPPORTED_FORMATS))
        raise InputValidationError(
            f"Unsupported model format '{model_format}'. Expected one of: {supported}"
        )
    return normalized

