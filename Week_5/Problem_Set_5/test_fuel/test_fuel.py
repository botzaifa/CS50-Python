import pytest
from fuel import convert, gauge

def test_convert_valid_input():
    assert convert("50/100") == 50
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("100/100") == 100

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("abc/def")
    with pytest.raises(ValueError):
        convert("10/5")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("100/50")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
