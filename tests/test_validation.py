from pathlib import Path

import pytest
from zenthrix.exceptions import InputValidationError
from zenthrix.validation import validate_model_format, validate_model_path


def test_validate_model_format_normalizes_case() -> None:
    assert validate_model_format("ONNX") == "onnx"


def test_validate_model_format_rejects_unknown_format() -> None:
    with pytest.raises(InputValidationError, match="Unsupported model format"):
        validate_model_format("safetensors")


def test_validate_model_path_rejects_directory(tmp_path: Path) -> None:
    with pytest.raises(InputValidationError, match="not a file"):
        validate_model_path(tmp_path)
