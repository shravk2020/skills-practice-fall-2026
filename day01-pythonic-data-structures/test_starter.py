from starter import get_even_squares, build_name_lookup, pair_with_index


def test_get_even_squares_basic():
    assert get_even_squares([1, 2, 3, 4, 5, 6]) == [4, 16, 36]


def test_get_even_squares_no_evens():
    assert get_even_squares([1, 3, 5]) == []


def test_get_even_squares_empty():
    assert get_even_squares([]) == []


def test_build_name_lookup_basic():
    assert build_name_lookup([(1, "Alice"), (2, "Bob")]) == {1: "Alice", 2: "Bob"}


def test_build_name_lookup_empty():
    assert build_name_lookup([]) == {}


def test_build_name_lookup_duplicate_id_last_wins():
    assert build_name_lookup([(1, "Alice"), (1, "Alicia")]) == {1: "Alicia"}


def test_pair_with_index_basic():
    assert pair_with_index(["a", "b", "c"]) == ["0: a", "1: b", "2: c"]


def test_pair_with_index_empty():
    assert pair_with_index([]) == []
