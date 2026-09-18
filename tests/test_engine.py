from pathlib import Path

import pytest
from zenthrix import Engine, EngineUnavailableError


def test_engine_validates_model_path(tmp_path: Path) -> None:
    model = tmp_path / "model.zx"
    model.write_bytes(b"placeholder")
    assert Engine(model).model_path == model


def test_engine_reports_missing_runtime(tmp_path: Path) -> None:
    model = tmp_path / "model.zx"
    model.write_bytes(b"placeholder")

    with pytest.raises(EngineUnavailableError, match="native engine"):
        Engine(model).generate("hello")


def test_engine_rejects_non_finite_temperature(tmp_path: Path) -> None:
    model = tmp_path / "model.zx"
    model.write_bytes(b"placeholder")

    with pytest.raises(ValueError, match="finite"):
        Engine(model).generate("hello", temperature=float("nan"))


def test_engine_rejects_non_compiled_model(tmp_path: Path) -> None:
    model = tmp_path / "model.onnx"
    model.write_bytes(b"placeholder")

    with pytest.raises(ValueError, match=".zx compiled model"):
        Engine(model)
