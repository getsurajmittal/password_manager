import hashlib
import os

password = "password123"

# Without salt: the same every time, and easy to look up
plain = hashlib.sha256(password.encode()).hexdigest()
print("No salt:  ", plain)

# With salt: 16 random bytes, different every run
salt = os.urandom(16)
salted = hashlib.sha256(salt + password.encode()).hexdigest()
print("Salt:     ", salt.hex())
print("With salt:", salted)