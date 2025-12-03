import argparse
import os

from algorithms import railfence
from algorithms import morse
from algorithms import des_module

def main():
    print("Welcome to our Encryption/Decryption Tool!\n")
    # Choose algorithm
    print("Select the algorithm:"
          +"\n1 - Rail Fence"
          +"\n2 - Morse Code"
          +"\n3 - DES")
    
    algo_choice = input("Enter the algorithm number: ").strip()

    if algo_choice == "1":
        algo = "railfence"
    elif algo_choice == "2":
        algo = "morse"
    elif algo_choice == "3":
        algo = "des"
    else:
        print("Invalid choice!")
        return

    # Choose operation
    print("\nSelect the operation:")
    print("1 - Encrypt")
    print("2 - Decrypt")
    
    mode_choice = input("Enter the operation number: ").strip()
    if mode_choice == "1":
        mode = "encrypt"
    elif mode_choice == "2":
        mode = "decrypt"
    else:
        print("Invalid choice!")
        return

    # Input text
    text = input("\nEnter the text: ").strip()

    # Additional settings based on algorithm
    if algo == "railfence":
        rails = input("Enter the number of Rails: ").strip()
        if not rails.isdigit():
            print("Number of Rails must be a valid integer!")
            return
        rails = int(rails)
        result = (
            railfence.encrypt(text, rails)
            if mode == "encrypt"
            else railfence.decrypt(text, rails)
        )

    elif algo == "morse":
        result = (
            morse.encrypt(text)
            if mode == "encrypt"
            else morse.decrypt(text)
        )

    elif algo == "des":
        key = input("Enter the DES key: ").strip()
        if not key:
            print("Key cannot be empty!")
            return
        result = (
            des_module.encrypt(text, key)
            if mode == "encrypt"
            else des_module.decrypt(text, key)
        )

    print("\nResult:" + result)
    print("\nOperation completed successfully!")

if __name__ == "__main__":
    main()
