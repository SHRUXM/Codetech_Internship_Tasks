from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os

def derive_key(password, salt=None):
    """Derives a secure key from the user's password."""

    if salt is None:
        salt = os.urandom(16)  # Generate a fresh salt

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,  # Key length for AES-256
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_file(input_file_path, password, output_file_path=None):
    """Encrypts a file using AES-256."""

    key, salt = derive_key(password)
    f = Fernet(key)

    try:
        with open(input_file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        if output_file_path is None:
            output_file_path = input_file_path + ".enc"
        with open(output_file_path, "wb") as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        print(f"Encryption error: {e}")
        return False

def decrypt_file(encrypted_file_path, password, output_file_path=None, salt=None):
    """Decrypts an encrypted file."""

    key, _ = derive_key(password, salt)  # Use the same salt
    f = Fernet(key)

    try:
        with open(encrypted_file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)

        if output_file_path is None:
            output_file_path = encrypted_file_path.replace(".enc", "")  # Or a safer default
        with open(output_file_path, "wb") as file:
            file.write(decrypted_data)
        return True
    except Exception as e:
        print(f"Decryption error: {e}")
        return False