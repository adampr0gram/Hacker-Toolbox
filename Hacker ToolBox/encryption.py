from cryptography.fernet import Fernet

def run():
    # Generate a key and cipher
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Ask user for input
    msg = input("Enter a message: ")

    # Encrypt and decrypt
    encrypted = cipher.encrypt(msg.encode())
    decrypted = cipher.decrypt(encrypted)

    # Show results
    print("\nEncrypted:", encrypted.decode())
    print("Decrypted:", decrypted.decode())
