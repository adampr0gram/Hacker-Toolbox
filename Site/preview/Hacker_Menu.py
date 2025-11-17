from js import document
import password_checker, port_scanner, brute_force, encryption

TOOLS = {
    "1": ("Password Strength Checker", password_checker.run),
    "2": ("Port Scanner (local only)", port_scanner.run),
    "3": ("Brute-Force", brute_force.run),
    "4": ("Encrypt Text", encryption.run),
}

def run_tool(tool_func, name):
    print(f"\nRunning {name}...\n")
    try:
        tool_func()
    except Exception as e:
        print(f"[ERROR] Failed to run tool: {e}")

def show_menu():
    container = document.getElementById("output")
    container.textContent = ""  # clear previous output

    menu_div = document.createElement("div")
    menu_div.className = "menu"

    title = document.createElement("h2")
    title.innerHTML = "Hacker Toolbox"
    menu_div.appendChild(title)

    for key, (name, func) in TOOLS.items():
        btn = document.createElement("button")
        btn.innerHTML = f"{key}. {name}"
        def handler(ev, func=func, name=name):
            run_tool(func, name)
        btn.addEventListener("click", handler)
        menu_div.appendChild(btn)

    container.appendChild(menu_div)

show_menu()
