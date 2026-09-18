# Changelog

All notable changes to Zenthrix are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-09-18

### Added

- Installable Python package published to PyPI.
- `zenthrix` command-line entry point with `compile`, `inspect`, and `run`
  commands.
- Typed public API with `Engine`, `InferenceResult`, and explicit error types.
- Input validation boundaries for ONNX, PyTorch Export/AOTInductor, and GGUF
  model inputs.
- Clear integration boundary for the separately distributed native compiler
  and runtime engine.
- CI checks for supported Python versions, linting, type checking, tests, and
  package builds.
- GitHub release workflow with PyPI trusted publishing support.
- `uv` development workflow with a committed lockfile.

### Notes

- Compilation and inference require the separately provisioned native engine;
  the public frontend does not include that proprietary binary.

[0.1.0]: https://github.com/withbrian-technologies/zenthrix/releases/tag/v0.1.0
