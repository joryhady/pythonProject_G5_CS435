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
- Select from multiple input files for decryption per algorithm

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
│ ├── rail_input.txt
│ ├── rail_enc.txt
│ ├── morse_input.txt
│ ├── morse_enc.txt
│ ├── des_input.txt
│ ├── des_enc.txt
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
For encryption, the tool always reads from input file (rail_input.txt/ morse_input.txt/ des_input.txt) and writes output to enc.txt.
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
## 1.Rail Fence Cipher:
Encrypts and decrypts text using a zigzag pattern across the specified number of rails.
Multiple input files supported for decryption (rail_input.txt, rail_enc.txt, rail_extra.txt).
## 2. Morse Code:
Morse Cipher turns letters and numbers into dots . and dashes -. Spaces between words are written as /, and dose not require any key.
-Encrypt a file(morse_input.txt):
python tool.py --algo morse --mode encrypt --infile mores_input.txt --outfile enc.txt
-Decrypt a file(mores_enc.txt):
python tool.py --algo morse --mode decrypt --infile morse_enc.txt --outfile decrypted.txt
Additional input files supported (morse_input.txt, morse_enc.txt, morse_extra.txt)
## 3. DES (Data Encryption Standard):
A symmetric-key block cipher using 8-byte keys.
-How to run it and ENCRYPT file(des_input.txt) open terminal and run this:
python tool.py --algo des --mode encrypt --infile des_input.txt --outfile enc.txt --key "12345678"
-How to decrypt file(des_enc.txt):
python tool.py --algo des --mode decrypt --infile des_enc.txt --outfile decrypted.txt --key "12345678"


## Testing:
# Rail Fence:
 - rail_input.txt:
Hello everyone this is just a test for Rail Fence Algorithm.
 - rail_enc.txt:
HvestregmeeentijaeoRFnlolorosutsfalcArtlyistiei.
# Morse Code:
 - morse_input.txt:
OKAY this is the testing for morse algorithm.
 - morse_enc.txt:
--- -.- .- -.-- / - .... .. ... / .. ... / - .... . /
. ... - .. -. --. / ..-. --- .-. / -- --- .-. ... . / 
.- .-.. --. --- .-. .. - .... --

# DES:
 - des_input.txt:
Hello jojo is testing her algorithm des.
 - des_enc.txt: 
cd96cff8dafc92e5c7605eb004712f6aabf8230eba36dc42fcc
356a7a48fea8fa0fb0d69a3d07876

All algorithms successfully encrypt and decrypt the input text.


## Group (5), The Members names (Section F1): 

- Jory Hady Alharbi  
- Amnah Abdullah Mukhtar 
- Afnan Amin  
- Rawan AL-balawi 
- Dima Alchehabi
- Lama Alhujouri 


## For any issues, call the team leader:
## jory email me at (joryhadialharbi@gmail.com) 
