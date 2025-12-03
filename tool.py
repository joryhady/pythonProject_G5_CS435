import argparse
import os

import argparse
import os

# tool.py 
from algorithms import reilfence
from algorithms import morse
from algorithms import des_module

def main():
    print("Welcome to Group 5 Encryption/Decryption Tool!")

    while True:
        print("\nSelect the algorithm:")
        print("1 - Rail Fence")
        print("2 - Morse Code")
        print("3 - DES")
        print("4 - Exit")
        
        algo_choice = input("Enter the algorithm number: ").strip()
        if algo_choice == "1":
            algo = "railfence"
        elif algo_choice == "2":
            algo = "morse"
        elif algo_choice == "3":
            algo = "des"
        elif algo_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            continue  

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
            continue

        text = input("\nEnter the text: ").strip()

        if algo == "railfence":
            rails = input("Enter the number of Rails: ").strip()
            if not rails.isdigit() or int(rails) < 2:
                print("Number of Rails must be an integer >= 2!")
                continue
            rails = int(rails)
            result = (
                reilfence.encrypt(text, rails)
                if mode == "encrypt"
                else reilfence.decrypt(text, rails)
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
                continue
            result = (
                des_module.encrypt(text, key)
                if mode == "encrypt"
                else des_module.decrypt(text, key)
            )

        print("\nResult:"+ result)
        print("\n-----------------------------------")

if __name__ == "__main__":
    main()
