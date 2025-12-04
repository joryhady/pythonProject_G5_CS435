import os
from algorithms import railfence
from algorithms import morse
from algorithms import des_module

# Default input files for ENCRYPTION per algorithm
DEFAULT_INPUT = {
    "railfence": "rail_input.txt",
    "morse": "morse_input.txt",
    "des": "des_input.txt"
}

# File options for DECRYPTION per algorithm
FILE_OPTIONS = {
    "railfence": [
        ("rail_input.txt", "Original text"),
        ("rail_enc.txt", "Encrypted Rail Fence"),
        ("rail_extra.txt", "Additional Rail Fence file")
    ],
    "morse": [
        ("morse_input.txt", "Original Morse text"),
        ("morse_enc.txt", "Encrypted Morse code"),
        ("morse_extra.txt", "Extra Morse file")
    ],
    "des": [
        ("des_input.txt", "Original DES text"),
        ("des_enc.txt", "Encrypted DES output"),
        ("des_extra.txt", "Extra DES file")
    ]
}


def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' does not exist!")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_and_print(text, output_file):
    print("\nResult:")
    print(text)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nOperation completed! Output saved in '{output_file}'")


def encrypt_text(text, algo, key=None, rails=None):
    if algo == "railfence":
        return railfence.encrypt(text, rails)
    elif algo == "morse":
        return morse.encrypt(text)
    elif algo == "des":
        return des_module.encrypt(text, key)
    else:
        raise ValueError("Unknown algorithm!")


def decrypt_text(text, algo, key=None, rails=None):
    if algo == "railfence":
        return railfence.decrypt(text, rails)
    elif algo == "morse":
        return morse.decrypt(text)
    elif algo == "des":
        return des_module.decrypt(text, key)
    else:
        raise ValueError("Unknown algorithm!")


def choose_algorithm():
    print("\nSelect the algorithm:")
    print("1 - Rail Fence")
    print("2 - Morse Code")
    print("3 - DES")
    print("4 - Exit")
    return input("Algorithm number: ").strip()


def choose_operation():
    print("\nSelect operation:")
    print("1 - Encrypt")
    print("2 - Decrypt")
    return input("Operation number: ").strip()


def choose_decrypt_file(algo):
    files = FILE_OPTIONS[algo]
    print("\nSelect file to decrypt:")
    for i, (fname, desc) in enumerate(files, start=1):
        print(f"{i} - {fname} ({desc})")
    while True:
        choice = input("File number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1][0]
        else:
            print(f"Invalid choice! Enter a number between 1 and {len(files)}.")


def main():
    print("Welcome to Group 5 Encryption/Decryption Tool!\n")

    while True:
        algo_choice = choose_algorithm()

        if algo_choice == "1":
            algo = "railfence"
            while True:
                rails = input("Enter number of Rails (>=2): ").strip()
                if rails.isdigit() and int(rails) >= 2:
                    rails = int(rails)
                    break
                else:
                    print("Invalid number of Rails! Must be integer >= 2.")
            key = None

        elif algo_choice == "2":
            algo = "morse"
            rails = None
            key = None

        elif algo_choice == "3":
            algo = "des"
            while True:
                key = input("Enter DES key (8 characters): ").strip()
                if len(key) >= 1:
                    break
                else:
                    print("Key cannot be empty!")
            rails = None

        elif algo_choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
            continue

        mode_choice = choose_operation()

        if mode_choice == "1":
            mode = "encrypt"
            input_file = DEFAULT_INPUT.get(algo)
            if input_file is None:
                print("No default input file configured for this algorithm.")
                continue
            # For encryption we save to the corresponding enc file (2nd listed file) when available
            output_file = FILE_OPTIONS[algo][1][0] if len(FILE_OPTIONS[algo]) > 1 else "enc.txt"

        elif mode_choice == "2":
            mode = "decrypt"
            input_file = choose_decrypt_file(algo)
            output_file = "dec.txt"

        else:
            print("Invalid operation!")
            continue

        # Read input file
        try:
            text = read_file(input_file)
        except FileNotFoundError as e:
            print(e)
            print("Make sure the input file exists or choose another file.")
            continue

        try:
            if mode == "encrypt":
                result = encrypt_text(text, algo, key, rails)
            else:
                result = decrypt_text(text, algo, key, rails)
        except Exception as e:
            print(f"Error during {mode}: {e}")
            continue

        save_and_print(result, output_file)
        print("\n-----------------------------------\n")


if __name__ == "__main__":
    main()