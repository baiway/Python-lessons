def is_palindrome(text):
    """Returns `True` if `text` reads the same forwards and backwards,
    ignoring capital letters and spaces"""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("racecar"))            # True
print(is_palindrome("level"))              # True
print(is_palindrome("python"))             # False
print(is_palindrome("Never odd or even"))  # True
