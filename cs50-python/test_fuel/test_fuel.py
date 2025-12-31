from fuel import convert, gauge
import pytest


def test_convert_valid_fraction():
    assert convert("3/4") == 75


def test_convert_exception():
    with pytest.raises(ValueError):
        assert convert("cat")
    with pytest.raises(ValueError):
        assert convert("1.2/3.4")
    with pytest.raises(ValueError):
        assert convert("-1/3")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
