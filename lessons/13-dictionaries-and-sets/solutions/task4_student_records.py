students = [
    {"name": "Ada", "year": 10, "scores": [72, 85, 64]},
    {"name": "Alan", "year": 11, "scores": [90, 78, 88]},
    {"name": "Grace", "year": 10, "scores": [65, 70, 71]},
    {"name": "Tim", "year": 11, "scores": [81, 93, 77]},
]

for student in students:
    mean = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}'s mean score is {mean:.1f}")

print("Students in Year 10:")
for student in students:
    if student["year"] == 10:
        print(f"  {student['name']}")
