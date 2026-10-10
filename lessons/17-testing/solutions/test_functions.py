import pytest

from functions import is_even, max_of_three, mean


# is_even
def test_even_numbers():
    assert is_even(2)
    assert is_even(100)


def test_odd_numbers():
    assert not is_even(1)
    assert not is_even(99)


def test_zero_is_even():
    assert is_even(0)


def test_negative_numbers():
    assert is_even(-4)
    assert not is_even(-3)


# max_of_three
def test_max_in_each_position():
    assert max_of_three(3, 2, 1) == 3
    assert max_of_three(1, 3, 2) == 3
    assert max_of_three(1, 2, 3) == 3


def test_max_with_ties():
    assert max_of_three(5, 5, 1) == 5
    assert max_of_three(1, 5, 5) == 5
    assert max_of_three(5, 1, 5) == 5
    assert max_of_three(4, 4, 4) == 4


def test_max_of_negative_numbers():
    assert max_of_three(-4, -2, -9) == -2


# mean
def test_mean():
    assert mean([1, 2, 3, 4]) == pytest.approx(2.5)
    assert mean([72, 85, 64]) == pytest.approx(73.6666667)


def test_mean_of_one_number():
    assert mean([7]) == 7


def test_mean_of_empty_list():
    # The mean of an empty list doesn't make sense. Our function raises a
    # ZeroDivisionError, because len([]) is 0. It might be better to raise a
    # ValueError with a helpful message instead, but either way, it shouldn't
    # return a number!
    with pytest.raises(ZeroDivisionError):
        mean([])
