from js import document
from cryptography.fernet import Fernet

def run():
    container = document.getElementById("output")
    container.textContent = ""  # clear previous output

    # Generate a key and cipher
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Create input field
    field = document.createElement("input")
    field.type = "text"
    field.placeholder = "Enter a message"
    container.appendChild(field)

    # Create button
    btn = document.createElement("button")
    btn.innerHTML = "Encrypt & Decrypt"
    container.appendChild(btn)

    # Handler
    def process(ev):
        msg = field.value
        encrypted = cipher.encrypt(msg.encode()).decode()
        decrypted = cipher.decrypt(encrypted.encode()).decode()

        container.textContent = (
            f"Original: {msg}\n\n"
            f"Encrypted: {encrypted}\n\n"
            f"Decrypted: {decrypted}"
        )

    btn.addEventListener("click", process)
