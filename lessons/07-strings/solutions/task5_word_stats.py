sentence = input("Enter a sentence: ")
words = sentence.split()

# Find the longest word and the total number of letters
longest = ""
total_length = 0
for word in words:
    total_length = total_length + len(word)
    if len(word) > len(longest):
        longest = word

print(f"Number of words: {len(words)}")
print(f"Longest word: {longest}")
print(f"Mean word length: {total_length / len(words):.2f}")
