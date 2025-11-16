import re
from js import document

def check_password(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"[0-9]", pw): score += 1
    if re.search(r"[!@#$%^&*()_+]", pw): score += 1

    levels = {
        0: "Extremely weak",
        1: "Very weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very strong"
    }
    return levels[score]

def run():
    container = document.getElementById("output")
    container.textContent = ""  # clear previous output

    # Create input field
    field = document.createElement("input")
    field.type = "text"
    field.placeholder = "Enter a password"
    container.appendChild(field)

    # Create button
    btn = document.createElement("button")
    btn.innerHTML = "Check Strength"
    container.appendChild(btn)

    # Handler
    def check(ev):
        pw = field.value
        result = check_password(pw)
        container.textContent = f"Password strength: {result}"

    btn.addEventListener("click", check)
