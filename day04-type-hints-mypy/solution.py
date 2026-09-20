def add_numbers(a: int, b: int) -> int:
    return a + b


def get_first_word(s: str) -> str:
    return s.split()[0]


def safe_divide(a: int, b: int) -> int | None:
    if b == 0:
        return None
    return a // b
