def clean(word):
    """Converts `word` to lowercase and removes any spaces"""
    return word.lower().replace(" ", "")


def are_anagrams(word1, word2):
    """Checks whether two words are anagrams by sorting their letters"""
    return sorted(clean(word1)) == sorted(clean(word2))


def are_anagrams_by_counting(word1, word2):
    """Checks whether two words are anagrams by counting each letter"""
    word1 = clean(word1)
    word2 = clean(word2)
    if len(word1) != len(word2):
        return False

    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False
    return True


print(are_anagrams("listen", "silent"))                       # True
print(are_anagrams("Dormitory", "dirty room"))                # True
print(are_anagrams("hello", "world"))                         # False
print(are_anagrams_by_counting("listen", "silent"))           # True
print(are_anagrams_by_counting("Dormitory", "dirty room"))    # True
print(are_anagrams_by_counting("aab", "abb"))                 # False
