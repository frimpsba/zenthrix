import json
from pathlib import Path

from zenthrix.cli import build_parser, main


def test_parser_accepts_compile_options() -> None:
    args = build_parser().parse_args(
        [
            "compile",
            "--model",
            "model.onnx",
            "--format",
            "onnx",
            "--output",
            "model.zx",
        ]
    )
    assert args.command == "compile"
    assert args.model_format == "onnx"


def test_inspect_reports_missing_native_engine(capsys, tmp_path: Path) -> None:
    model = tmp_path / "model.zx"
    model.write_bytes(b"placeholder")

    assert main(["inspect", str(model), "--memory-profile"]) == 2
    assert "native engine" in capsys.readouterr().err


def test_run_reports_json_error(capsys, tmp_path: Path) -> None:
    model = tmp_path / "model.zx"
    model.write_bytes(b"placeholder")

    assert (
        main(
            [
                "run",
                "--model",
                str(model),
                "--prompt",
                "hello",
                "--json",
            ]
        )
        == 2
    )
    payload = json.loads(capsys.readouterr().out)
    assert payload["error"] == "EngineUnavailableError"
    assert "native engine" in payload["message"]


def test_inspect_rejects_non_compiled_model(capsys, tmp_path: Path) -> None:
    model = tmp_path / "model.onnx"
    model.write_bytes(b"placeholder")

    assert main(["inspect", str(model)]) == 2
    assert ".zx compiled model" in capsys.readouterr().err


def test_compile_reports_missing_native_engine(tmp_path: Path, capsys) -> None:
    model = tmp_path / "model.onnx"
    model.write_bytes(b"placeholder")

    assert (
        main(
            [
                "compile",
                "--model",
                str(model),
                "--format",
                "onnx",
                "--output",
                str(tmp_path / "model.zx"),
            ]
        )
        == 2
    )
    assert "native compiler engine" in capsys.readouterr().err


def test_compile_rejects_invalid_output_extension(tmp_path: Path, capsys) -> None:
    model = tmp_path / "model.onnx"
    model.write_bytes(b"placeholder")

    assert (
        main(
            [
                "compile",
                "--model",
                str(model),
                "--format",
                "onnx",
                "--output",
                str(tmp_path / "model.bin"),
            ]
        )
        == 2
    )
    assert ".zx extension" in capsys.readouterr().err
