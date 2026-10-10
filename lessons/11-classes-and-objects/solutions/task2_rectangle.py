class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 5)

print(r1.area(), r1.perimeter(), r1.is_square())  # 12 14 False
print(r2.area(), r2.perimeter(), r2.is_square())  # 25 20 True
