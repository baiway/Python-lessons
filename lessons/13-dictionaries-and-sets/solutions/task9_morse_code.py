MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
}

# Swap the keys and values, so we can look letters up by their Morse code
FROM_MORSE = {code: letter for letter, code in MORSE.items()}


def encode(message):
    """Encodes `message` in Morse code. Characters other than letters and
    spaces are ignored."""
    encoded_words = []
    for word in message.upper().split():
        codes = [MORSE[letter] for letter in word if letter in MORSE]
        encoded_words.append(" ".join(codes))
    return " / ".join(encoded_words)


def decode(code):
    """Decodes a message written in Morse code"""
    decoded_words = []
    for word in code.split(" / "):
        letters = [FROM_MORSE[symbol] for symbol in word.split()]
        decoded_words.append("".join(letters))
    return " ".join(decoded_words)


secret = encode("Hello world")
print(secret)  # .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(decode(secret))  # HELLO WORLD
