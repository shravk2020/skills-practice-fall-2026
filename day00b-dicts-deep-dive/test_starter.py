from starter import (
    get_or_default,
    increment_count,
    merge_configs,
    pop_or_default,
    invert,
    common_keys,
)


def test_get_or_default_present():
    assert get_or_default({"a": 1}, "a", 0) == 1


def test_get_or_default_missing():
    d = {"a": 1}
    assert get_or_default(d, "z", 0) == 0
    assert d == {"a": 1}  # unchanged


def test_increment_count_new_key():
    counts = {}
    increment_count(counts, "x")
    assert counts == {"x": 1}


def test_increment_count_existing_key():
    counts = {"x": 3}
    increment_count(counts, "x")
    assert counts == {"x": 4}


def test_merge_configs_override_wins():
    base = {"theme": "light", "font_size": 12}
    override = {"font_size": 14}
    result = merge_configs(base, override)
    assert result == {"theme": "light", "font_size": 14}
    assert base == {"theme": "light", "font_size": 12}  # unchanged
    assert override == {"font_size": 14}  # unchanged


def test_pop_or_default_present():
    d = {"a": 1, "b": 2}
    result = pop_or_default(d, "a", None)
    assert result == 1
    assert d == {"b": 2}


def test_pop_or_default_missing():
    d = {"a": 1}
    result = pop_or_default(d, "z", "fallback")
    assert result == "fallback"
    assert d == {"a": 1}


def test_invert():
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_common_keys():
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 99, "c": 100, "d": 101}
    assert common_keys(d1, d2) == {"b", "c"}
