import hashlib
text1 = "password123"
encrypted1 = hashlib.sha256(text1.encode()).hexdigest()
print(encrypted1)