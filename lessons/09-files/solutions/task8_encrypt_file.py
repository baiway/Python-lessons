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


with open("message.txt", encoding="utf-8") as file:
    message = file.read()

with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(caesar_encrypt(message, 7))

print("Encrypted message.txt and saved it to encrypted.txt")
