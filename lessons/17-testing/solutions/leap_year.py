def is_leap_year(year):
    """Returns `True` if `year` is a leap year"""
    # The original version forgot about years divisible by 400 (like 2000),
    # which ARE leap years, even though they're divisible by 100
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
