# Contributing

## Local setup

Use Python 3.10 or newer and install the development tools:

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install pytest ruff mypy build
```

Alternatively, use `uv` to create the environment and install the declared
development dependency group:

```bash
uv sync
```

Run the checks before opening a pull request:

```bash
python -m ruff check .
python -m mypy python
python -m pytest
python -m build
```

With `uv`, run the same checks in the project environment:

```bash
uv run ruff check .
uv run mypy python
uv run pytest
uv run python -m build
```

The public package validates model inputs and exposes the CLI/API boundary.
Compilation and inference require the separately distributed native engine.
