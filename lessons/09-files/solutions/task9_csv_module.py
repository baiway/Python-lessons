import csv

# With `.split(",")`, the line `"Turing, Alan","fish, chips and mushy peas"`
# would be split into FOUR values, because there are commas inside the quotes:
#   ['"Turing', ' Alan"', '"fish', ' chips and mushy peas"']
# The `csv` module understands the quotes, so it gives us the two values we want.
with open("people.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip the header
    for row in reader:
        name = row[0]
        food = row[1]
        print(f"{name}'s favourite food is {food}")
