"""ONNX input validation."""

from pathlib import Path

from ..exceptions import InputValidationError
from ..validation import validate_model_path


def validate_onnx(path: str | Path) -> Path:
    """Validate an ONNX model path without importing optional ONNX tooling."""
    model_path = validate_model_path(path)
    if model_path.suffix.lower() != ".onnx":
        raise InputValidationError(f"Expected an .onnx file, got: {model_path}")
    return model_path
