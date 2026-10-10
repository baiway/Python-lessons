class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def mean_score(self):
        return sum(self.scores) / len(self.scores)


names = ["Ada", "Alan", "Grace", "Tim"]
scores = [
    [72, 85, 64],  # Ada
    [90, 78, 88],  # Alan
    [65, 70, 71],  # Grace
    [81, 93, 77],  # Tim
]

# Create a Student object for each name, and give them their scores
students = []
for i in range(len(names)):
    student = Student(names[i])
    for score in scores[i]:
        student.add_score(score)
    students.append(student)

# Print each student's mean score, keeping track of the best student
best = students[0]
for student in students:
    print(f"{student.name}'s mean score is {student.mean_score():.1f}")
    if student.mean_score() > best.mean_score():
        best = student

print(f"{best.name} has the highest mean score")
