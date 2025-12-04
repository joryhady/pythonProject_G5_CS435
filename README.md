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
The main program is tool.py. This tool allows users to encrypt or decrypt text messages stored in a file using one of three cryptographic algorithms: Rail Fence, Morse Code, or DES.
Steps:
- Open the the file 'tool.py' and run it.
- Select the algorithm: Rail Fence, Morse Code, or DES
- Provide additional parameters if required (Rails or DES key), Algorithm-specific Inputs:
Rail Fence: User enters the number of rails (integer ≥ 2).
DES: User enters a key (string, 8 characters recommended).
Morse Code: No additional input required.
- Choose the operation: Encrypt or Decrypt
For encryption, the tool always reads from input.txt and writes output to enc.txt.
For decryption, the tool asks which file to decrypt.
- Result:
The resulting encrypted or decrypted text is printed to the screen.
The result is also saved to the respective output file (enc.txt or dec.txt).

Example:

Welcome to Group 5 Encryption/Decryption Tool!

Select the algorithm:

1 - Rail Fence

2 - Morse Code

3 - DES

4 - Exit

Enter the algorithm number: 1

Enter the number of Rails: 3

Select the operation:

1 - Encrypt

2 - Decrypt

Enter the operation number: 1

Result:

HOLELWRDLO

Operation completed! Output saved in 'enc.txt'


# Algorithms Are:
## 1.
## 2. Morse Code:
Morse Cipher turns letters and numbers into dots . and dashes -. Spaces between words are written as /, and dose not require any key.
-Encrypt a file(input.txt):
python tool.py --algo morse --mode encrypt --infile input.txt --outfile enc.txt
-Decrypt a file(enc.txt):
python tool.py --algo morse --mode decrypt --infile enc.txt --outfile decrypted.txt
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
- Rawan AL-balawi 
- Dima Alchehabi
- Lama Alhujouri 


## For any issues, call the team leader jory email me at (joryhadialharbi@gmail.com) 
