from argon2 import PasswordHasher
ph = PasswordHasher()

password = ph.hash("suraj@123")
# print(password)

try:
    ph.verify(password,"suraj@123")
    # print("correct password")
except Exception:
    print("error")

try:
    ph.verify(password,"suraj@@123")
    # print("correct password")
except Exception:
    print("error")