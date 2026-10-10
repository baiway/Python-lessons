import math


def sphere_surface_area(radius):
    """Calculates the surface area of a sphere with the given radius"""
    return 4 * math.pi * radius**2


def is_even(n):
    """Returns `True` if `n` is even and `False` otherwise"""
    return n % 2 == 0


def mean(numbers):
    """Returns the mean of a list of numbers"""
    return sum(numbers) / len(numbers)


def linear_search(items, target):
    """Returns the index of `target` in `items`, or -1 if it isn't there"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def make_username(first_name, surname, year):
    """Returns a username made from the first three letters of `surname`, the
    first letter of `first_name` and the last two digits of `year`"""
    return surname[:3].lower() + first_name[0].lower() + str(year)[-2:]


def count_words(text):
    """Returns a dictionary mapping each word in `text` to how many times it
    appears"""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def greet(name, greeting="Hello"):
    """Prints a greeting"""
    print(f"{greeting}, {name}!")


print(sphere_surface_area(2.0))
print(is_even(7))
print(mean([1, 2, 3, 4]))
print(linear_search(["a", "b", "c"], "c"))
print(make_username("Ada", "Lovelace", 2026))
print(count_words("the cat sat on the mat"))
greet("Ada")
