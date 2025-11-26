# algorithms/morse.py

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}

REVERSE_MORSE = {v: k for k, v in MORSE_DICT.items()}


def encrypt(text):
    text = text.upper()
    encrypted = []

    for char in text:
        if char == " ":
            encrypted.append("/")   # Slash for word separator
        elif char in MORSE_DICT:
            encrypted.append(MORSE_DICT[char])
        else:
            encrypted.append("?")   # Unknown char

    return " ".join(encrypted)


def decrypt(morse_code):
    words = morse_code.split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded = ""

        for symbol in letters:
            decoded += REVERSE_MORSE.get(symbol, "?")

        decoded_words.append(decoded)

    return " ".join(decoded_words)
