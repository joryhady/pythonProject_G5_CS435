# CS435 – Cryptography Project  
## Group 5 – Text File Encryption and Decryption Tool

This project is for CS435 Cryptography course at Taibah University.  
The goal is to implement a tool that encrypts and decrypts text files using 3 Algorithms (Group 5):

- Rail Fence Cipher (Algorithm 5)  
- Morse Code (Algorithm 7)  
- DES – Data Encryption Standard (Algorithm 12)

## Project Description
This tool allows users to:

- Encrypt plaintext stored inside text files  
- Decrypt ciphertext using the selected algorithm  
- Choose between three algorithms (Rail Fence, Morse, DES)  
- Provide keys (for DES and Rail Fence)  
- Use a Command-Line Interface (CLI)

The program reads from an input text file and writes the results to an output file.

---

## Project Structure:
CS435_Group5/
│
├── tool.py
│
├── algorithms/
│ ├── railfence.py
│ ├── morse.py
│ ├── des_module.py
│
├── examples/
│ ├── sample_input.txt
│ ├── sample_output.txt
│
└── README.md

## Installation:
Jory in DES Algorithm needed an external library which was:
PyCryptodome for DES.

## Usage (CLI):
The main program is `tool.py`.

# Algorithms Are:
## 1.
## 2. Morse Code:
Morse Cipher turns letters and numbers into dots . and dashes -. Spaces between words are written as /.
## 3. DES (Data Encryption Standard):
A symmetric-key block cipher using 8-byte keys.
-How to run it and ENCRYPT file(input.txt) open terminal and run this:
python tool.py --algo des --mode encrypt --infile input.txt --outfile enc.txt --key "12345678"
-How to decrypt file(enc.txt):
python tool.py --algo des --mode decrypt --infile enc.txt --outfile decrypted.txt --key "12345678"


## Testing:


## Group (5), The Members names (Section F1): 

- Jory Hady Alharbi  
- Amnah Abdullah Mukhtar 
- Afnan Amin  
- Member 4  
- Member 5  
- Member 6 

## For any issues, call the team leader jory(0500415233).
