import os
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def derive_key(password, salt):
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID,
    )


salt = os.urandom(16)
master_password = "suraj_master"

key = derive_key(master_password,salt)
secret = "suraj@123"
nonce = os.urandom(12)
ciphertext = AESGCM(key).encrypt(nonce, secret.encode(), None)

print(f'secret --> {secret}')
print(f'key --> {key.hex()}')
print(f'nonce --> {nonce.hex()}')
print(f'salt --> {salt.hex()}')
print(f'ciphertext-->{ciphertext.hex()}')

print(f'decrypted --> {AESGCM(key).decrypt(nonce, ciphertext, None).decode()}')