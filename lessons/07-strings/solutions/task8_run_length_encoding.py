def rle_encode(text):
    """Compresses `text` using run-length encoding"""
    if text == "":
        return ""

    encoded = ""
    current = text[0]
    run_length = 1
    for char in text[1:]:
        if char == current:
            run_length = run_length + 1
        else:
            # The run has ended, so record it and start a new one
            encoded = encoded + str(run_length) + current
            current = char
            run_length = 1

    # Don't forget the final run!
    return encoded + str(run_length) + current


def rle_decode(text):
    """Decompresses text that was compressed using run-length encoding"""
    decoded = ""
    digits = ""  # collects the digits of the current number, e.g. "12"
    for char in text:
        if char.isdigit():
            digits = digits + char
        else:
            decoded = decoded + char * int(digits)
            digits = ""
    return decoded


print(rle_encode("AAAABBBCCD"))   # 4A3B2C1D
print(rle_decode("4A3B2C1D"))     # AAAABBBCCD

long_run = "W" * 12 + "B" + "W" * 3
print(rle_encode(long_run))                          # 12W1B3W
print(rle_decode(rle_encode(long_run)) == long_run)  # True
