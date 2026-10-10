# Read a CSV file into two lists
names = []
scores = []
with open("scores.csv", encoding="utf-8") as file:
    for line in file:
        values = line.strip().split(",")
        names.append(values[0])
        scores.append(int(values[1]))

print(names)
print(scores)

# Add 5 bonus points to everyone, then write the new scores to a new CSV file
for i in range(len(scores)):
    scores[i] = scores[i] + 5

with open("new_scores.csv", "w", encoding="utf-8") as file:
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
