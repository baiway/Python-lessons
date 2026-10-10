names = ["Ada", "Alan", "Grace", "Tim"]
scores = [
    [72, 85, 64],  # Ada
    [90, 78, 88],  # Alan
    [65, 70, 71],  # Grace
    [81, 93, 77],  # Tim
]

# 1. Each student's mean score (the mean of each row). We store these in a
#    list so we can use them again in part 3.
student_means = []
for i in range(len(names)):
    mean = sum(scores[i]) / len(scores[i])
    student_means.append(mean)
    print(f"{names[i]}'s mean score is {mean:.1f}")

# 2. The mean score for each test (the mean of each column)
num_tests = len(scores[0])
for test in range(num_tests):
    total = 0
    for row in scores:
        total = total + row[test]
    print(f"The mean score for test {test + 1} is {total / len(scores):.1f}")

# 3. The student with the highest mean score
best = 0
for i in range(len(student_means)):
    if student_means[i] > student_means[best]:
        best = i
print(f"{names[best]} has the highest mean score")
