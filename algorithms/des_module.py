from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES Algorithm by jory hady
def encrypt(text, key):
    key = key.encode("utf-8")[:8].ljust(8, b'0')
    cipher = DES.new(key, DES.MODE_ECB)
    # KEY must be 8 bytes,
    # here it's block cipher,
    # so each block would be encrypted with the same key
    encrypted = cipher.encrypt(pad(text.encode(), DES.block_size))
    return encrypted.hex()

def decrypt(hex_text, key):
    key = key.encode("utf-8")[:8].ljust(8, b'0')
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(bytes.fromhex(hex_text)), DES.block_size)
    return  decrypted.decode()


