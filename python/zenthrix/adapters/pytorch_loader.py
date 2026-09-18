"""PyTorch Export/AOTInductor input validation."""

from pathlib import Path

from ..validation import validate_model_path


def validate_pytorch_export(path: str | Path) -> Path:
    """Validate a PyTorch export artifact path."""
    return validate_model_path(path)

