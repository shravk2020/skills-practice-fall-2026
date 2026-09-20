def add_numbers(a, b):
    """TODO: add type hints. Both parameters and the return value are ints."""
    return a + b


def get_first_word(s: str) -> int:
    """TODO: fix the return type hint -- it's wrong for what this actually
    returns. Run mypy to see exactly what it expects instead.
    """
    return s.split()[0]


def safe_divide(a: int, b: int) -> int:
    """TODO: this function can return None (when b is 0), but the return
    type hint claims it always returns an int. Fix the hint to reflect
    reality -- don't change the behavior.
    """
    if b == 0:
        return None
    return a // b
