import itertools
from starter import read_large_numbers, first_n_over_threshold, group_consecutive_duplicates


def test_read_large_numbers_is_a_generator():
    result = read_large_numbers(5)
    assert iter(result) is result, "should return a generator, not a list"


def test_read_large_numbers_values():
    assert list(read_large_numbers(5)) == [1, 4, 9, 16, 25]


def test_first_n_over_threshold_with_list():
    assert first_n_over_threshold([1, 5, 2, 8, 3, 9], threshold=4, n=2) == [5, 8]


def test_first_n_over_threshold_with_infinite_generator():
    infinite = itertools.count(1)
    assert first_n_over_threshold(infinite, threshold=100, n=3) == [101, 102, 103]


def test_group_consecutive_duplicates():
    assert group_consecutive_duplicates([1, 1, 2, 2, 2, 3, 1, 1]) == [
        (1, 2), (2, 3), (3, 1), (1, 2),
    ]


def test_group_consecutive_duplicates_empty():
    assert group_consecutive_duplicates([]) == []


def test_group_consecutive_duplicates_no_repeats():
    assert group_consecutive_duplicates([1, 2, 3]) == [(1, 1), (2, 1), (3, 1)]
