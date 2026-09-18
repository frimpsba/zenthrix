"""Command-line interface for the Zenthrix frontend."""

import argparse
import sys

from . import __version__
from .engine import Engine
from .exceptions import ZenthrixError
from .validation import (
    validate_compile_options,
    validate_compiled_model_path,
    validate_model_input,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(prog="zenthrix")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)

    compile_parser = commands.add_parser("compile", help="Compile a model")
    compile_parser.add_argument("--model", required=True)
    compile_parser.add_argument("--format", required=True, dest="model_format")
    compile_parser.add_argument("--target", default="auto")
    compile_parser.add_argument("--quantization")
    compile_parser.add_argument("--output", required=True)

    inspect_parser = commands.add_parser("inspect", help="Inspect a compiled model")
    inspect_parser.add_argument("model")
    inspect_parser.add_argument("--memory-profile", action="store_true")

    run_parser = commands.add_parser("run", help="Run inference")
    run_parser.add_argument("--model", required=True)
    run_parser.add_argument("--prompt", required=True)
    run_parser.add_argument("--max-tokens", type=int, default=128)
    run_parser.add_argument("--temperature", type=float, default=0.2)
    return parser


def _compile(args: argparse.Namespace) -> int:
    validate_model_input(args.model, args.model_format)
    validate_compile_options(args.target, args.quantization, args.output)
    raise ZenthrixError(
        "The native compiler engine is not installed. "
        "The public frontend cannot produce a .zx binary yet."
    )


def _inspect(args: argparse.Namespace) -> int:
    model_path = validate_compiled_model_path(args.model)
    print(f"Model: {model_path}")
    print("Memory profile: unavailable until the native engine is installed")
    return 0


def _run(args: argparse.Namespace) -> int:
    result = Engine(args.model).generate(
        args.prompt,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    print(result.text)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    args = build_parser().parse_args(argv)
    try:
        if args.command == "compile":
            return _compile(args)
        if args.command == "inspect":
            return _inspect(args)
        if args.command == "run":
            return _run(args)
    except (ZenthrixError, ValueError) as error:
        print(f"zenthrix: error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
