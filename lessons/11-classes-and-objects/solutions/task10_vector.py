import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)                  # (4, 6)
print(v1 * 3)                   # (9, 12)
print(v1.magnitude())           # 5.0
print(v1 == Vector(3, 4))       # True
print(v1 == v2)                 # False

# Without `__eq__`, `v1 == Vector(3, 4)` would be False! By default, `==`
# checks whether two objects are the SAME object, not whether they have the
# same attributes. `v1` and `Vector(3, 4)` are two different objects that
# happen to contain the same values.
