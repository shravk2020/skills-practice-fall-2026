import time
import functools


def timer(func):
    """A decorator that prints how long `func` took to run, then returns
    func's normal return value unchanged.

    TODO: implement. Use time.perf_counter() before and after calling func.
    Print something like: f"{func.__name__} took {elapsed:.4f}s"
    Don't forget functools.wraps(func) on your inner function.
    """
    return func


def retry(times=3):
    """A decorator factory. The decorated function is called; if it raises
    an exception, it's retried, up to `times` total attempts (not `times`
    retries in addition to the first call). If it still fails on the last
    attempt, let the exception propagate.

    TODO: implement `decorator` and its inner `wrapper`.
    """
    def decorator(func):
        return func
    return decorator
