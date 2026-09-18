"""Exceptions raised by the public Zenthrix frontend."""


class ZenthrixError(Exception):
    """Base class for expected Zenthrix errors."""


class InputValidationError(ZenthrixError, ValueError):
    """Raised when a user-provided path or option is invalid."""


class EngineUnavailableError(ZenthrixError, RuntimeError):
    """Raised when the private native compilation engine is not installed."""

