from starter import (
    unique_words,
    shared_tags,
    only_in_first,
    clean_sentence,
    split_first_rest,
    title_case_sentence,
)


def test_unique_words():
    assert unique_words("the Cat sat on the MAT") == {"the", "cat", "sat", "on", "mat"}


def test_shared_tags():
    assert shared_tags(["python", "ml", "web"], ["ml", "web", "docker"]) == {"ml", "web"}


def test_shared_tags_none_in_common():
    assert shared_tags(["a"], ["b"]) == set()


def test_only_in_first():
    assert only_in_first(["a", "b", "c"], ["b"]) == {"a", "c"}


def test_clean_sentence():
    assert clean_sentence("  Hello World  ") == "hello world"


def test_split_first_rest():
    assert split_first_rest([1, 2, 3, 4]) == (1, [2, 3, 4])


def test_split_first_rest_single_item():
    assert split_first_rest([1]) == (1, [])


def test_title_case_sentence():
    assert title_case_sentence("the quick brown fox") == "The Quick Brown Fox"
