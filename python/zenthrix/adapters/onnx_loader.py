"""ONNX input validation."""

from pathlib import Path

from ..validation import validate_model_path


def validate_onnx(path: str | Path) -> Path:
    """Validate an ONNX model path without importing optional ONNX tooling."""
    model_path = validate_model_path(path)
    if model_path.suffix.lower() != ".onnx":
        raise ValueError(f"Expected an .onnx file, got: {model_path}")
    return model_path
