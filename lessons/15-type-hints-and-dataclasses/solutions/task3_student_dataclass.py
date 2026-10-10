from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)

    def add_score(self, score: int) -> None:
        self.scores.append(score)

    def mean_score(self) -> float:
        return sum(self.scores) / len(self.scores)


names = ["Ada", "Alan", "Grace", "Tim"]
scores = [
    [72, 85, 64],  # Ada
    [90, 78, 88],  # Alan
    [65, 70, 71],  # Grace
    [81, 93, 77],  # Tim
]

students = [Student(names[i], scores[i]) for i in range(len(names))]

best = students[0]
for student in students:
    print(f"{student.name}'s mean score is {student.mean_score():.1f}")
    if student.mean_score() > best.mean_score():
        best = student

print(f"{best.name} has the highest mean score")
print(best)  # thanks to `@dataclass`, this prints something useful
