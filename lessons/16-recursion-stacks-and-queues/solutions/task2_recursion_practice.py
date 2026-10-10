def power(base, exponent):
    """Calculates base**exponent, for whole numbers exponent >= 0"""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def sum_digits(n):
    """Adds up the digits of the whole number `n`"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def reverse(text):
    """Reverses a string"""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


print(power(2, 10))       # 1024
print(power(5, 0))        # 1
print(sum_digits(1234))   # 10
print(sum_digits(7))      # 7
print(reverse("hello"))   # olleh
print(reverse(""))        # (an empty string)
