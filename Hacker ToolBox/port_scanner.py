import socket

def scan(target, ports):
    print(f"\n=== SAFE EDUCATIONAL PORT SCAN ===")
    print(f"Target: {target}")
    print("IMPORTANT: Only scan systems you own or have explicit permission to test!\n")

    for port in ports:
        s = socket.socket()
        s.settimeout(0.2)

        try:
            s.connect((target, port))
            print(f"[OPEN]   Port {port}")
        except:
            print(f"[CLOSED] Port {port}")
        finally:
            s.close()

def run():
    target_ip = input("Enter target IP/Domain: ").strip()

    # Safe default ports (common, harmless to check)
    ports_to_check = [21, 22, 80, 443, 3306, 8080]

    print("\nScanning...\n")
    scan(target_ip, ports_to_check)

    input("\nDone. Press ENTER to return to menu...")
