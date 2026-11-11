import hashlib
import time
from argon2 import PasswordHasher

password = "password123"

# SHA-256: how many guesses per second?
start = time.perf_counter()
for _ in range(100_000):
    hashlib.sha256(password.encode()).digest()
elapsed = time.perf_counter() - start
print(f"SHA-256: {100_000 / elapsed:,.0f} guesses per second")

# Argon2: how many guesses per second?
ph = PasswordHasher()
start = time.perf_counter()
for _ in range(10):
    ph.hash(password)
elapsed = time.perf_counter() - start
print(f"Argon2:  {10 / elapsed:,.1f} guesses per second")