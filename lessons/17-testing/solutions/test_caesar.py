import pytest

from caesar import caesar_decrypt, caesar_encrypt


@pytest.mark.parametrize("message, shift, expected", [
    ("abc", 1, "bcd"),
    ("xyz", 3, "abc"),              # wraps around the end of the alphabet
    ("ABC", 3, "DEF"),              # capital letters stay capital
    ("Hello, World!", 3, "Khoor, Zruog!"),  # spaces and punctuation are unchanged
    ("abc", 0, "abc"),              # a shift of 0 does nothing
    ("abc", 26, "abc"),             # neither does a shift of 26
    ("abc", -1, "zab"),             # negative shifts go backwards
    ("", 5, ""),                    # an empty message
])
def test_encrypt(message, shift, expected):
    assert caesar_encrypt(message, shift) == expected


@pytest.mark.parametrize("message", [
    "Hello, World!",
    "The quick brown fox jumps over the lazy dog",
    "ZEBRAS & zebras",
    "",
])
@pytest.mark.parametrize("shift", [1, 3, 13, 25, 100])
def test_decrypt_reverses_encrypt(message, shift):
    # Stacking two `parametrize` decorators tests every combination!
    assert caesar_decrypt(caesar_encrypt(message, shift), shift) == message
