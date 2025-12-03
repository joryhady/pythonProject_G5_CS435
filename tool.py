import argparse
import os
# tool.py 
from algorithms import reilfence
from algorithms import morse
from algorithms import des_module

INPUT_FILE = "input.txt" 

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
        return reilfence.encrypt(text, rails)
    elif algo == "morse":
        return morse.encrypt(text)
    elif algo == "des":
        return des_module.encrypt(text, key)
    else:
        raise ValueError("Unknown algorithm!")

def decrypt_text(text, algo, key=None, rails=None):
    if algo == "railfence":
        return reilfence.decrypt(text, rails)
    elif algo == "morse":
        return morse.decrypt(text)
    elif algo == "des":
        return des_module.decrypt(text, key)
    else:
        raise ValueError("Unknown algorithm!")

def main():
    print("Welcome to Group 5 Encryption/Decryption Tool!\n")

    while True:
        # Algorithm selection
        print("\nSelect the algorithm:")
        print("1 - Rail Fence")
        print("2 - Morse Code")
        print("3 - DES")
        print("4 - Exit")
        algo_choice = input("Algorithm number: ").strip()

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

        # Operation selection
        print("\nSelect operation:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        mode_choice = input("Operation number: ").strip()

        if mode_choice == "1":
            mode = "encrypt"
            input_file = INPUT_FILE
            output_file = "enc.txt"
        elif mode_choice == "2":
            mode = "decrypt"
            # Ask user which file to decrypt
            while True:
                print("\nSelect file to decrypt:")
                print("1 - input.txt")
                print("2 - enc.txt")
                file_choice = input("File number: ").strip()
                if file_choice == "1":
                    input_file = "input.txt"
                    break
                elif file_choice == "2":
                    input_file = "enc.txt"
                    break
                else:
                    print("Invalid choice! Enter 1 or 2.")
            output_file = "dec.txt"
        else:
            print("Invalid operation!")
            continue

        # Read input file
        try:
            text = read_file(input_file)
        except FileNotFoundError as e:
            print(e)
            continue


        try:
            if mode == "encrypt":
                result = encrypt_text(text, algo, key, rails)
            else:
                result = decrypt_text(text, algo, key, rails)
        except Exception as e:
            print(f"Error during {mode}: {e}")
            continue

        # Show and save result
        save_and_print(result, output_file)

        print("\n-----------------------------------\n")

if __name__ == "__main__":
    main()
