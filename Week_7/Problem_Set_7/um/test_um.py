import pytest
from um import count

def test_count_um():
    assert count("hello, um, world") == 1
    assert count("Hello, Um, World") == 1
    assert count("yummy") == 0
    assert count("um um um") == 3
    assert count("") == 0


def test_count_um_with_punctuation():
    assert count("hello, um!") == 1
    assert count("hello, Um?") == 1
    assert count("hello, um.") == 1


def test_count_um_with_multiple_words():
    assert count("um hello um world") == 2
    assert count("hello um world um") == 2


pytest.main([__file__, "-v"])