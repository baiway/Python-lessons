def shift_letter(letter, shift):
    """Shifts a single letter `shift` places along the alphabet, wrapping
    around from Z to A. Anything that isn't a letter is left unchanged."""
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    else:
        return letter

    position = ord(letter) - start
    new_position = (position + shift) % 26
    return chr(start + new_position)


def caesar_encrypt(message, shift):
    """Encrypts `message` using a Caesar cipher"""
    encrypted = ""
    for letter in message:
        encrypted = encrypted + shift_letter(letter, shift)
    return encrypted


def caesar_decrypt(message, shift):
    """Decrypts a message that was encrypted with a Caesar cipher"""
    return caesar_encrypt(message, -shift)


with open("encrypted.txt", encoding="utf-8") as file:
    encrypted = file.read()

print(caesar_decrypt(encrypted, 7))
