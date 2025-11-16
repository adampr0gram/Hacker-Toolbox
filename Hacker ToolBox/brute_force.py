import socket
import itertools
import time

def run():
    HOST = input("Enter IP Address: ")
    PORT = 5000

    # Characters to try (demo)
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!#$%^&*()-=];',./_[+|}:<{>?"

    attempts = 0
    found = False

    # Try passwords of increasing length
    for length in range(1, 50):  # safer demo: 1–5 letters
        for combo in itertools.product(chars, repeat=length):
            password = "".join(combo)
            attempts += 1

            try:
                s = socket.socket()
                s.settimeout(0.5)
                s.connect((HOST, PORT))
                s.send(password.encode())
                response = s.recv(1024).decode()
                s.close()

                print(f"Trying '{password}' -> {response}")

                if response == "SUCCESS":
                    print(f"\nPassword FOUND: {password} in {attempts} attempts")
                    found = True
                    break
            except Exception as e:
                print(f"Connection failed: {e}")
                break
        if found:
            break
