def is_leap_year(year):
    """Returns `True` if `year` is a leap year"""
    return year % 4 == 0 and year % 100 != 0
