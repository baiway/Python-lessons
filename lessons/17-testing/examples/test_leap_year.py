from leap_year import is_leap_year


def test_normal_leap_year():
    assert is_leap_year(2024)


def test_normal_year():
    assert not is_leap_year(2023)


def test_century():
    assert not is_leap_year(1900)


def test_400_years():
    assert is_leap_year(2000)
