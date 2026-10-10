# 1. Read the high scores into a 2D list
high_scores = []
with open("high_scores.csv", encoding="utf-8") as file:
    for line in file:
        values = line.strip().split(",")
        high_scores.append([values[0], int(values[1])])

# 2. Get the new score
name = input("Player name: ")
score = int(input("Score: "))

# 3. Find the first score that the new score beats, and insert it there. If it
#    doesn't beat any of them, it goes at the end.
position = len(high_scores)
for i in range(len(high_scores)):
    if score > high_scores[i][1]:
        position = i
        break
high_scores.insert(position, [name, score])

# 4. Keep only the top 5
high_scores = high_scores[:5]

# 5. Save and print the new high score table
with open("high_scores.csv", "w", encoding="utf-8") as file:
    for row in high_scores:
        file.write(f"{row[0]},{row[1]}\n")

print("High scores:")
for i, row in enumerate(high_scores, start=1):
    print(f"{i}. {row[0]:<10} {row[1]:>6}")
