import pytest
from starter import NegativeValueError, require_non_negative, suppress_and_log


def test_require_non_negative_passes_through():
    assert require_non_negative(5) == 5
    assert require_non_negative(0) == 0


def test_require_non_negative_raises():
    with pytest.raises(NegativeValueError):
        require_non_negative(-1)


def test_suppress_and_log_suppresses_listed_exception(capsys):
    with suppress_and_log(ValueError):
        raise ValueError("boom")
    # if we get here, the exception was suppressed -- success
    captured = capsys.readouterr()
    assert "Suppressed" in captured.out
    assert "boom" in captured.out


def test_suppress_and_log_suppresses_one_of_several_types():
    with suppress_and_log(ValueError, KeyError):
        raise KeyError("missing")
    # no exception escaped -- success


def test_suppress_and_log_does_not_suppress_other_types():
    with pytest.raises(TypeError):
        with suppress_and_log(ValueError):
            raise TypeError("not in the list")


def test_suppress_and_log_no_exception_at_all():
    ran = False
    with suppress_and_log(ValueError):
        ran = True
    assert ran is True
