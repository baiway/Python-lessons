import datetime

today = str(datetime.date.today())
entry = input("How did your day go? ")

# Append mode adds to the end of the file, so old entries are kept
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(f"{today}: {entry}\n")

print("Diary entry saved!")
