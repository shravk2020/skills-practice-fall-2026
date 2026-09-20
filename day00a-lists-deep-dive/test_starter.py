from starter import (
    add_if_missing,
    combine,
    take_last,
    every_other_reversed,
    remove_and_return_middle,
    safe_index,
    sort_by_length_desc,
    independent_copy,
)


def test_add_if_missing_adds_new_value():
    items = [1, 2, 3]
    result = add_if_missing(items, 4)
    assert result == [1, 2, 3, 4]
    assert items == [1, 2, 3, 4]  # mutated in place


def test_add_if_missing_ignores_existing_value():
    items = [1, 2, 3]
    result = add_if_missing(items, 2)
    assert result == [1, 2, 3]


def test_combine_does_not_mutate_inputs():
    a = [1, 2]
    b = [3, 4]
    result = combine(a, b)
    assert result == [1, 2, 3, 4]
    assert a == [1, 2]
    assert b == [3, 4]


def test_take_last_basic():
    assert take_last([1, 2, 3, 4, 5], 2) == [4, 5]


def test_take_last_zero():
    assert take_last([1, 2, 3], 0) == []


def test_every_other_reversed():
    assert every_other_reversed([1, 2, 3, 4, 5, 6]) == [6, 4, 2]


def test_remove_and_return_middle():
    items = [1, 2, 3, 4, 5]
    middle = remove_and_return_middle(items)
    assert middle == 3
    assert items == [1, 2, 4, 5]


def test_safe_index_found():
    assert safe_index(["a", "b", "c"], "b") == 1


def test_safe_index_not_found():
    assert safe_index(["a", "b", "c"], "z") == -1


def test_sort_by_length_desc_does_not_mutate():
    words = ["a", "ccc", "bb"]
    result = sort_by_length_desc(words)
    assert result == ["ccc", "bb", "a"]
    assert words == ["a", "ccc", "bb"]


def test_independent_copy():
    original = [1, 2, 3]
    copy = independent_copy(original)
    copy.append(4)
    assert original == [1, 2, 3]
    assert copy == [1, 2, 3, 4]
