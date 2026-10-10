import pytest

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_minus_forty():
    # -40 is the same in both scales!
    assert celsius_to_fahrenheit(-40) == -40
    assert fahrenheit_to_celsius(-40) == -40


def test_round_trip():
    # Floats have tiny rounding errors, so check the answer is approximately 37
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == pytest.approx(37)
