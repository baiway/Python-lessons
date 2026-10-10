# Write a few lines to a file. "w" mode deletes anything already in the file!
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("eggs\n")
    file.write("milk\n")
    file.write("bread\n")

# Read it back to check that it worked
with open("shopping.txt", encoding="utf-8") as file:
    print(file.read())
