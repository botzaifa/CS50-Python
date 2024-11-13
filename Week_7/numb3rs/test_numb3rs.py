import pytest
from numb3rs import validate

# Test cases for valid IPv4 addresses
@pytest.mark.parametrize("ip", [
    "192.168.1.1",
    "10.0.0.1",
    "255.255.255.255",
])
def test_valid_ipv4(ip):
    assert validate(ip) == True

# Test cases for invalid IPv4 addresses
@pytest.mark.parametrize("ip", [
    "256.168.1.1",    # Invalid range (first byte exceeds 255)
    "192.168.1.300",  # Invalid range (last byte exceeds 255)
    "192.168.1",      # Incomplete address
    "192.168.1.1.1",  # Extra byte
    "192.168.1.-1",   # Negative number
    "192.168.1.abc",  # Non-numeric characters
])
def test_invalid_ipv4(ip):
    assert validate(ip) == False

# Test case for incorrect IPv4 format
def test_incorrect_format():
    assert validate("192.168.1") == False  # Missing the last byte

# Test case for partially correct IPv4 format
def test_partial_format():
    assert validate("192.168.1.") == False  # Incomplete address

# Test case for edge case: all zeros
def test_all_zeros():
    assert validate("0.0.0.0") == True

# Test case for edge case: all 255s
def test_all_255s():
    assert validate("255.255.255.255") == True
