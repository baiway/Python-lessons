import math


def sphere_surface_area(radius: float) -> float:
    """Calculates the surface area of a sphere with the given radius"""
    return 4 * math.pi * radius**2


def is_even(n: int) -> bool:
    """Returns `True` if `n` is even and `False` otherwise"""
    return n % 2 == 0


def mean(numbers: list[float]) -> float:
    """Returns the mean of a list of numbers"""
    return sum(numbers) / len(numbers)


def linear_search(items: list[str], target: str) -> int:
    """Returns the index of `target` in `items`, or -1 if it isn't there"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def make_username(first_name: str, surname: str, year: int) -> str:
    """Returns a username made from the first three letters of `surname`, the
    first letter of `first_name` and the last two digits of `year`"""
    return surname[:3].lower() + first_name[0].lower() + str(year)[-2:]


def count_words(text: str) -> dict[str, int]:
    """Returns a dictionary mapping each word in `text` to how many times it
    appears"""
    # mypy can't work out what type an empty dictionary should be, so we tell it
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def greet(name: str, greeting: str = "Hello") -> None:
    """Prints a greeting"""
    print(f"{greeting}, {name}!")


print(sphere_surface_area(2.0))
print(is_even(7))
print(mean([1, 2, 3, 4]))  # mypy is happy to treat ints as floats
print(linear_search(["a", "b", "c"], "c"))
print(make_username("Ada", "Lovelace", 2026))
print(count_words("the cat sat on the mat"))
greet("Ada")
