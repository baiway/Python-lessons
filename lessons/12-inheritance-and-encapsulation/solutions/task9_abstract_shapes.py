import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Every subclass of Shape MUST define this method"""

    def describe(self):
        print(f"A {self.name} with area {self.area():.2f}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("triangle")
        self.base = base
        self.height = height
    # Oops! We forgot to define `area`...


for shape in [Rectangle(3, 4), Circle(2)]:
    shape.describe()

# We can't create a plain Shape, because it's abstract...
try:
    Shape("blob")
except TypeError as error:
    print(f"Error: {error}")

# ...and we can't create a Triangle either, because it doesn't define `area`.
# Python catches this mistake as soon as we try to create one, rather than
# waiting until we call `area`.
try:
    Triangle(3, 4)
except TypeError as error:
    print(f"Error: {error}")
