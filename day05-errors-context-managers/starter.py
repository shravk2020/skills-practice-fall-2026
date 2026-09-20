class NegativeValueError(Exception):
    """Raised when a negative value is passed where only non-negative is allowed."""
    pass


def require_non_negative(n):
    """Raise NegativeValueError if n < 0, otherwise return n unchanged.

    TODO: implement.
    """
    pass


class suppress_and_log:
    """A context manager. Takes one or more exception classes.

    If the wrapped block raises one of those exception types, print
    f"Suppressed: {exception}" and prevent it from propagating.
    Any other exception type should propagate normally.

    TODO: implement __enter__ and __exit__.
    """

    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass
