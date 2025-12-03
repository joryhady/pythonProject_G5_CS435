# Morse Code Cipher-By Amnah

MORSE_TABLE = {
"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
"Z": "--..",
"0": "-----", "1": ".----", "2": "..---", "3": "...--",
"4": "....-", "5": ".....", "6": "-....", "7": "--...",
"8": "---..", "9": "----."
}

# Reverse 
MORSE_REVERSE = {code: ch for ch, code in MORSE_TABLE.items()}


def encrypt(text: str) -> str:

text = text.upper()
output = []

for ch in text:
if ch == " ":
output.append("/") # Word separator
elif ch in MORSE_TABLE:
output.append(MORSE_TABLE[ch])
else:
output.append("#") # Unknown symbol

return " ".join(output)


def decrypt(morse: str) -> str:

words = morse.split(" / ")
decoded_words = []

for word in words:
letters = word.split()
current = ""

for symbol in letters:
current += MORSE_REVERSE.get(symbol, "#")
decoded_words.append(current)

return " ".join(decoded_words)
