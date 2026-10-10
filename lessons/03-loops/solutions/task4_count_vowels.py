text = input("Enter a word or sentence: ")

# Count the vowels (we use `.lower()` so that capital letters are counted too)
vowel_count = 0
for letter in text.lower():
    if letter in "aeiou":
        vowel_count = vowel_count + 1

print(f"'{text}' contains {vowel_count} vowels")
