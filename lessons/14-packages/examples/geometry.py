import math

def circle_area(radius):
    """Calculates the area of a circle with the given radius"""
    return math.pi * radius**2


def circle_circumference(radius):
    """Calculates the circumference of a circle with the given radius"""
    return 2 * math.pi * radius


if __name__ == "__main__":
    # This only runs if you run `python geometry.py`, not when you import it
    print(circle_area(1))
    print(circle_circumference(1))
