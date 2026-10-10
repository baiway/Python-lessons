score = int(input("Enter your score out of 100: "))

# Check from the highest boundary down. Because Python stops at the first
# true condition, we don't need to check e.g. `score < 80` in the second test.
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "U"

print(f"A score of {score} gets a grade {grade}")
