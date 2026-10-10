from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    year: int
    scores: list[int] = field(default_factory=list)

    def mean_score(self) -> float:
        return sum(self.scores) / len(self.scores)


@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0


@dataclass(frozen=True)
class Colour:
    red: int
    green: int
    blue: int


@dataclass(order=True)
class Version:
    major: int
    minor: int


# `@dataclass` writes `__init__`, `__repr__` and `__eq__` for us
ada = Student("Ada", 10, [72, 85, 64])
print(ada)
print(ada.mean_score())
print(ada == Student("Ada", 10, [72, 85, 64]))

# Each student gets their own empty list
alan = Student("Alan", 11)
grace = Student("Grace", 10)
alan.scores.append(90)
print(alan.scores, grace.scores)

# Default values
print(BankAccount("Tim"))

# Frozen dataclasses can't be changed, but can be used as dictionary keys
orange = Colour(255, 165, 0)
names = {orange: "orange"}
print(names[Colour(255, 165, 0)])

# Ordered dataclasses can be compared and sorted, attribute by attribute
versions = [Version(3, 12), Version(2, 7), Version(3, 9)]
print(sorted(versions))
