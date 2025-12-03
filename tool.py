import argparse
import os

# Import algorithms
from algorithms import railfence
from algorithms import morse
from algorithms import des_module

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

def main():
    parser = argparse.ArgumentParser(
        description="Group 5 - Text File Encryption/Decryption Tool"
    )

    parser.add_argument("--algo", required=True,
                        choices=["railfence", "morse", "des"])

    parser.add_argument("--mode", required=True,
                        choices=["encrypt", "decrypt"])

    parser.add_argument("--infile", required=True)
    parser.add_argument("--outfile", required=True)

    parser.add_argument("--key", help="Key for DES")
    parser.add_argument("--rails", type=int, help="Rails for Rail Fence")

    args = parser.parse_args()

    if not os.path.exists(args.infile):
        print("Error: Input file not found.")
        return

    text = read_file(args.infile)

    # RAILFENCE
    if args.algo == "railfence":
        if args.rails is None:
            print("Error: --rails is required for Rail Fence")
            return

        result = (
            railfence.encrypt(text, args.rails)
            if args.mode == "encrypt"
            else railfence.decrypt(text, args.rails)
        )

    # MORSE
    elif args.algo == "morse":
        result = (
            morse.encrypt(text)
            if args.mode == "encrypt"
            else morse.decrypt(text)
        )

    # DES
    elif args.algo == "des":
        if not args.key:
            print("Error: --key required for DES")
            return

        result = (
            des_module.encrypt(text, args.key)
            if args.mode == "encrypt"
            else des_module.decrypt(text, args.key)
        )

    else:
        print("Unknown algorithm.")
        return

    write_file(args.outfile, result)
    print(f"Success → Output file saved to: {args.outfile}")


if __name__ == "__main__":
    main()
