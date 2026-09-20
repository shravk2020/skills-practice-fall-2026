import time
import pytest
from starter import timer, retry


def test_timer_returns_correct_value():
    @timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_timer_prints_something(capsys):
    @timer
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() != ""


def test_timer_preserves_function_name():
    @timer
    def add(a, b):
        return a + b

    assert add.__name__ == "add"


def test_retry_succeeds_without_needing_a_retry():
    calls = {"count": 0}

    @retry(times=3)
    def always_works():
        calls["count"] += 1
        return "ok"

    assert always_works() == "ok"
    assert calls["count"] == 1


def test_retry_succeeds_after_two_failures():
    calls = {"count": 0}

    @retry(times=3)
    def fails_twice_then_succeeds():
        calls["count"] += 1
        if calls["count"] < 3:
            raise ValueError("not yet")
        return "ok"

    assert fails_twice_then_succeeds() == "ok"
    assert calls["count"] == 3


def test_retry_raises_after_exhausting_all_attempts():
    calls = {"count": 0}

    @retry(times=2)
    def always_fails():
        calls["count"] += 1
        raise ValueError("nope")

    with pytest.raises(ValueError):
        always_fails()
    assert calls["count"] == 2


def test_retry_preserves_function_name():
    @retry(times=3)
    def my_func():
        return "ok"

    assert my_func.__name__ == "my_func"
