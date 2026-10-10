# Read the whole file into one string
with open("poem.txt", encoding="utf-8") as file:
    contents = file.read()

print(contents)

# Read the file one line at a time
with open("poem.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
