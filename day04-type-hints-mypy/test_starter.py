from starter import add_numbers, get_first_word, safe_divide


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_get_first_word():
    assert get_first_word("hello world") == "hello"


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) is None
