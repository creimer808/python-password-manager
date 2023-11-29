import hashlib
import secrets

def generate_salt():
    return secrets.token_hex(16)

def hash_password(password, salt):
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password