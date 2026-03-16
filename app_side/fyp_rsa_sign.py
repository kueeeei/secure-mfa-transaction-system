# Following after decryption
# RSA Sign in Flutter app
# Send "sign" back to server

from hashlib import sha256
from cryptography.hazmat.primitives import serialization

def hash_gen(transaction_text):
    h = sha256(transaction_text.encode('utf-8')).hexdigest()
    h_int = int(h, 16)

    return h_int

# s = h^d mod n
def rsa_sign(plaintext, sk_pem): 
    sk_obj = serialization.load_pem_private_key(
            sk_pem.encode(),
            password=None 
        )
    hash_int = hash_gen(plaintext)
    sk_nums = sk_obj.private_numbers()
    n = sk_nums.public_numbers.n 
    d = sk_nums.d   
    sign = pow(hash_int, d, n)

    return sign
    
        