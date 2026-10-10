# 1. Cubes of the numbers from 1 to 10
cubes = [i**3 for i in range(1, 11)]
print(cubes)

# 2. Multiples of 7 below 100
multiples_of_7 = [i for i in range(1, 100) if i % 7 == 0]
print(multiples_of_7)

# 3. Words containing the letter "o"
sentence = "the quick brown fox jumps over the lazy dog"
o_words = [word for word in sentence.split() if "o" in word]
print(o_words)

# 4. Numbers mapped to their squares
squares = {i: i**2 for i in range(1, 11)}
print(squares)

# 5. Vowels in "comprehension"
vowels = {letter for letter in "comprehension" if letter in "aeiou"}
print(sorted(vowels))
