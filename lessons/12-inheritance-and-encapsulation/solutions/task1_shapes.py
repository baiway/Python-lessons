import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

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


class Square(Rectangle):
    def __init__(self, side):
        # A square is a rectangle whose width and height are both `side`
        super().__init__(side, side)
        self.name = "square"


shapes = [Rectangle(3, 4), Circle(2), Square(5), Circle(0.5)]
for shape in shapes:
    shape.describe()
