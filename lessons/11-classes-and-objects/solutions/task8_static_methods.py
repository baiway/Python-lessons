class Rectangle:
    def __init__(self, width, height):
        if not Rectangle.is_valid_length(width) or not Rectangle.is_valid_length(height):
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    @staticmethod
    def is_valid_length(value):
        """Returns `True` if `value` is a positive number"""
        # `isinstance` checks whether `value` is an int or a float (we'll see
        # more of it in Lesson 12)
        return isinstance(value, (int, float)) and value > 0

    @classmethod
    def square(cls, side):
        """Creates a square with the given side length"""
        return cls(side, side)

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height


print(Rectangle.is_valid_length(3))    # True
print(Rectangle.is_valid_length(-2))   # False
print(Rectangle.is_valid_length("3"))  # False

square = Rectangle.square(5)
print(square.width, square.height, square.area(), square.is_square())  # 5 5 25 True

try:
    Rectangle(3, -4)
except ValueError as error:
    print(f"Error: {error}")
