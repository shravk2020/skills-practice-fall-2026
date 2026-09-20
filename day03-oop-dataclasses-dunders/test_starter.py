import pytest
from starter import Rectangle


def test_area_property():
    r = Rectangle(3, 4)
    assert r.area == 12


def test_area_updates_if_width_changes():
    r = Rectangle(3, 4)
    r.width = 5
    assert r.area == 20  # proves area is computed, not stored


def test_repr():
    r = Rectangle(3, 4)
    assert repr(r) == "Rectangle(width=3, height=4)"


def test_eq_true():
    assert Rectangle(3, 4) == Rectangle(3, 4)


def test_eq_false():
    assert Rectangle(3, 4) != Rectangle(1, 1)


def test_area_is_read_only():
    r = Rectangle(3, 4)
    with pytest.raises(AttributeError):
        r.area = 100
