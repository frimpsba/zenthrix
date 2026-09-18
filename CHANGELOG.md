# Changelog

All notable changes to Zenthrix are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Compile option validation for targets, quantization modes, and `.zx` output
  paths.

## [0.1.1] - 2026-09-18

### Added

- Format-specific adapter dispatch during CLI compilation validation.
- Extension checks for ONNX and GGUF inputs.
- Regression coverage for adapter dispatch and mismatched model inputs.

### Changed

- Bumped the package and public API version to `0.1.1`.

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
[0.1.1]: https://github.com/withbrian-technologies/zenthrix/releases/tag/v0.1.1
