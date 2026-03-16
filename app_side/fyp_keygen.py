# RSA Key generation (on flutter app)
# Public Key (e, n)
# Private key (e, d)

import secrets
from math import gcd
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def prime_check(n, k=40):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
        
    for each in range(k):
        a = secrets.randbelow(n - 4) + 2 #generate random int bewteen 2 to n-2
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = secrets.randbits(bits)
        p |= (1 << (bits - 1)) | 1
        if prime_check(p):
            return p

def export_keys_to_pem(n, e, d, p, q):
    if q > p:
        p, q = q, p

    dmp1 = pow(d, 1, p - 1)
    dmq1 = pow(d, 1, q - 1)
    iqmp = pow(q, -1, p)
    
    public_numbers = rsa.RSAPublicNumbers(e, n)
    private_key = rsa.RSAPrivateNumbers(
        p, q, d, dmp1, dmq1, iqmp, public_numbers
    ).private_key()

    # export private key
    pem_private = private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption() 
    )

    # export public key
    pem_public = private_key.public_key().public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem_private.decode(), pem_public.decode()

# key length: 4096 bits
def key_gen():
    bit_length = 2048
        
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    while p == q:
        q = generate_prime(bit_length)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    if gcd(e, phi) != 1:
        return key_gen()
                
    d = pow(e, -1, phi)

    private_pem, public_pem = export_keys_to_pem(n, e, d, p, q)

    print(f"Public Key: {public_pem}...")
    
    return private_pem, public_pem

if __name__ == "__main__":
    sk_pem, pk_pem = key_gen()