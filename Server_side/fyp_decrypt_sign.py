from cryptography.hazmat.primitives import serialization

def decrypt(cipher_hex, sk_pem):

    sk_obj = serialization.load_pem_private_key(
        sk_pem.encode(),
        password=None 
    )
    sk_nums = sk_obj.private_numbers()
    n = sk_nums.public_numbers.n 
    d = sk_nums.d
        
    cipher = int(cipher_hex, 16)

    # M = C^d mod n
    m_int = pow(cipher, d, n)
    m_bytes = m_int.to_bytes((m_int.bit_length() + 7) // 8, byteorder='big')

    try:
        plaintext = m_bytes.decode('utf-8')
    except UnicodeDecodeError:
        plaintext = "Decryption Failed."
    
    # print("\n--- Decrypted Message ---")
    # print(f"M = {plaintext}")
    return plaintext


def main():
    # cipher => read in from qrcode
    # sk_pem => get it from device secure space
    # result = decrypt(cipher, sk_pem)
    pass