# Verificaiton in Bank Server

# 1. Call origin_hash and public key pair
# 2. Decrypt sign value from flutter app
# 3. Compare saved_hash and decrypted_hash
#    Same => Success, not equal => Fail

from cryptography.hazmat.primitives import serialization

# verify = sign^e mod n
def verify(pk_pem, origin_hash, sign):

    pk_obj = serialization.load_pem_public_key(pk_pem.encode())
    pk_nums = pk_obj.public_numbers()
    n = pk_nums.n
    e = pk_nums.e

    verify = pow(sign, e, n)

    if origin_hash == verify:
        return True
    else:
        return False
    


