class MarkupError(Exception):
    """General execution error for markups."""


class MarkupAlreadyRegistered(Exception):
    """Raised when trying to register an already registered markup."""


class InvalidMarkup(Exception):
    """Raised when a markup is not subclassing BaseMarkup."""


class MarkupNotFound(Exception):
    """Raised when trying to look up a markup that was not registered."""
