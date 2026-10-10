ALPHABET = set("abcdefghijklmnopqrstuvwxyz")


def is_pangram(sentence):
    """Returns `True` if `sentence` contains every letter of the alphabet"""
    missing = ALPHABET - set(sentence.lower())
    if len(missing) > 0:
        print(f"Missing letters: {sorted(missing)}")
    return len(missing) == 0


print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello, world!"))                                 # False
