filename = input("Enter the name of a file: ")

try:
    with open(filename, encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, I couldn't find a file called '{filename}'.")
else:
    num_lines = len(contents.splitlines())  # `.splitlines()` splits on new lines
    num_words = len(contents.split())
    num_chars = len(contents)
    print(f"{filename} has {num_lines} lines, {num_words} words and {num_chars} characters.")
