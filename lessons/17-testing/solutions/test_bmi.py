import pytest

from bmi import calculate_bmi


def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.857, abs=0.001)
    assert calculate_bmi(50, 1.6) == pytest.approx(19.53125)


def test_zero_mass():
    with pytest.raises(ValueError, match="Mass must be greater than zero"):
        calculate_bmi(0, 1.75)


def test_negative_mass():
    with pytest.raises(ValueError, match="Mass must be greater than zero"):
        calculate_bmi(-70, 1.75)


def test_zero_height():
    with pytest.raises(ValueError, match="Height must be greater than zero"):
        calculate_bmi(70, 0)


def test_negative_height():
    with pytest.raises(ValueError, match="Height must be greater than zero"):
        calculate_bmi(70, -1.75)
