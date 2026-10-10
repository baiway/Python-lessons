import pytest

from fizzbuzz import fizzbuzz


def test_normal_numbers():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(7) == "7"


def test_multiples_of_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_multiples_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(20) == "Buzz"


def test_multiples_of_15():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


def test_zero_and_negative_numbers():
    # The game starts at 1, so I've decided that anything less than 1 is invalid
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-3)
