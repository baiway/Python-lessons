names = []
scores = []
with open("scores.csv", encoding="utf-8") as file:
    for line in file:
        values = line.strip().split(",")
        names.append(values[0])
        scores.append(int(values[1]))

for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")

# Find the index of the highest score
best = 0
for i in range(len(scores)):
    if scores[i] > scores[best]:
        best = i

print(f"Mean score: {sum(scores) / len(scores):.1f}")
print(f"Highest score: {names[best]} ({scores[best]})")
