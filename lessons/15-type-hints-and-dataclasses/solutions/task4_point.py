from dataclasses import FrozenInstanceError, dataclass
import math

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        """Returns the distance between this point and `other`"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


a = Point(0, 0)
b = Point(3, 4)
print(a.distance_to(b))  # 5.0

# We're breaking the rules on purpose here, so we tell mypy not to complain
try:
    a.x = 10  # type: ignore[misc]
except FrozenInstanceError as error:
    print(f"Error: {error}")

# Because points are frozen, they can be stored in sets
visited = {Point(0, 0), Point(1, 2), Point(0, 0)}
print(visited)  # only two points: the duplicate is ignored
