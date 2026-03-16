# 1. RSA Encryption
# 2. Generate Hash value with SHA256

import secrets
from cryptography.hazmat.primitives import serialization
from hashlib import sha256

# read in public key pair (n, e)
def encrypt(transaction_text, pk_pem):

    pk_obj = serialization.load_pem_public_key(pk_pem.encode())
    pk_nums = pk_obj.public_numbers()
    n = pk_nums.n
    e = pk_nums.e

    # convert text into binary
    trans_bytes = transaction_text.encode('utf-8')
    trans_int = int.from_bytes(trans_bytes, byteorder='big')
    
    # RSA encryption function: C = M^e mod n
    cipher_int = pow(trans_int, e, n)
    
    return hex(cipher_int)

# generate hash digest with sha256 for verification
# save digest into database.transaction.hash
def hash_gen(transaction_text):
    h = sha256(transaction_text.encode('utf-8')).hexdigest()
    h_int = int(h, 16)

    return h_int

if __name__ == "__main__":
    pass
    # transcation => the transcation info meed to be encrypted
    # pk_pem => read in from database.accounts.public_key

    # cipher = encrypt(transaction, pk_pem)
    # print(f"Ciphertext in Hex: {cipher}")