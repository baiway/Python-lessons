class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Points that are equal must have the same hash, so we hash a tuple of
        # exactly the attributes that `__eq__` compares
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


points = {Point(1, 2), Point(1, 2), Point(3, 4)}
print(len(points))             # 2
print(Point(1, 2) in points)   # True

names = {Point(0, 0): "origin"}
print(names[Point(0, 0)])      # origin

# Changing a point after adding it to a set breaks the set: the point is still
# stored in the slot for its OLD hash, so the set looks in the wrong slot
p = Point(5, 6)
points.add(p)
p.x = 50
print(Point(50, 6) in points)  # False, even though p is in the set!
print(p in points)             # also False
