import os
import password_checker
import port_scanner
import brute_force
import encryption

TOOLS = {
    "1": ("Password Strength Checker", password_checker.run),
    "2": ("Port Scanner (local only)", port_scanner.run),
    "3": ("Brute-Force", brute_force.run),
    "4": ("Encrypt Text", encryption.run),
    "0": ("Exit", None)
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_tool(tool_func):
    print("\nRunning tool...\n")
    try:
        tool_func()
    except Exception as e:
        print(f"[ERROR] Failed to run tool: {e}")

def main():
    while True:
        clear()
        print("====================================")
        print("   Hacker ToolBox  ")
        print("====================================\n")
        print("Select a tool:\n")
        # ✅ FIX: correctly unpack dictionary values
        for key, value in TOOLS.items():
            name = value[0]
            print(f"  {key}. {name}")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("\nGoodbye!")
            break

        if choice in TOOLS:
            name, tool_func = TOOLS[choice]
            if tool_func:
                run_tool(tool_func)
            input("\nPress ENTER to return to menu...")
        else:
            print("\nInvalid option!")
            input("Press ENTER to continue...")

if __name__ == "__main__":
    main()
