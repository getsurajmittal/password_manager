import os
from argon2.low_level import hash_secret_raw, Type

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
password = "suraj_master"

# key = derive_key("suraj_master",salt)
print(derive_key("suraj_master",salt).hex())
print(derive_key("suraj_master",salt).hex())
print(derive_key("suraj_masterr",salt).hex())