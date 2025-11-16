import re

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
    pw = input("Enter a password to test: ")
    print("Password strength:", check_password(pw))
