from js import document

def run():
    container = document.getElementById("output")
    container.textContent = ""  # clear previous output

    # Create input field for target
    field = document.createElement("input")
    field.type = "text"
    field.placeholder = "Enter target IP/Domain"
    container.appendChild(field)

    # Create button to start scan
    btn = document.createElement("button")
    btn.innerHTML = "Scan Ports"
    container.appendChild(btn)

    # Safe default ports
    ports_to_check = [21, 22, 80, 443, 3306, 8080]

    def scan(ev):
        target = field.value.strip()
        container.textContent = f"\n=== SAFE EDUCATIONAL PORT SCAN ===\nTarget: {target}\n"
        container.textContent += "IMPORTANT: This is a demo — browsers cannot perform real socket scans.\n\n"

        # Fake results for demonstration
        for port in ports_to_check:
            if port in (80, 443):
                container.textContent += f"[OPEN]   Port {port}\n"
            else:
                container.textContent += f"[CLOSED] Port {port}\n"

    btn.addEventListener("click", scan)
