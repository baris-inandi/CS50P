from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")
        assert convert("1/0")
        assert convert("5/0")
    with pytest.raises(ValueError):
        assert convert("2/1")
        assert convert("3/2")
        assert convert("5/1")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(42) == "42%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
