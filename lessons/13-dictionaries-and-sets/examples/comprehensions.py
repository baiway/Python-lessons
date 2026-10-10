# The long way...
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(squares)

# ...and the short way
squares = [i**2 for i in range(1, 6)]
print(squares)

# Comprehensions with a condition
words = ["python", "is", "a", "wonderful", "language"]
evens = [i for i in range(1, 21) if i % 2 == 0]
long_words = [word for word in words if len(word) > 5]
print(evens)
print(long_words)

# Dictionary and set comprehensions
lengths = {word: len(word) for word in ["cat", "giraffe", "emu"]}
first_letters = {word[0] for word in ["apple", "avocado", "banana"]}
print(lengths)
print(first_letters)
