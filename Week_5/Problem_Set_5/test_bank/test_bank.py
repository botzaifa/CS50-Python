import bank
import pytest


def test_starts_with_hello():
    assert bank.value("hello, world") == 0
    assert bank.value("HELLO, world") == 0
    assert bank.value("hello") == 0
    assert bank.value("Hello, how are you?") == 0


def test_starts_with_h():
    assert bank.value("hi there") == 20
    assert bank.value("H, what's up?") == 20
    assert bank.value("hola") == 20
    assert bank.value("h") == 20


def test_otherwise():
    assert bank.value("goodbye") == 100
    assert bank.value("123 hello") == 100
    assert bank.value("what's up?") == 100
    assert bank.value("") == 100


if __name__ == "__main__":
    pytest.main()
