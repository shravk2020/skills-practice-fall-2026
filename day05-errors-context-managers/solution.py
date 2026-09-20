class NegativeValueError(Exception):
    pass


def require_non_negative(n):
    if n < 0:
        raise NegativeValueError(f"expected non-negative, got {n}")
    return n


class suppress_and_log:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            print(f"Suppressed: {exc_value}")
            return True
        return False
