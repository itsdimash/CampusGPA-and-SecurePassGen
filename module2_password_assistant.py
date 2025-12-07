UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*+-"

def check_strength(pw):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for ch in pw:
        if ch in UPPERS:
            has_upper = True
        if ch in LOWERS:
            has_lower = True
        if ch in DIGITS:
            has_digit = True
        if ch in SYMBOLS:
            has_symbol = True
    if len(pw) >= 8:
        length_ok = True
    else:
        length_ok = False
    if length_ok and has_upper and has_lower and has_digit and has_symbol:
        all_ok = True
    else:
        all_ok = False

    report = {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "all_ok": all_ok
    }
    return report

def suggestions_for(pw):
    info = check_strength(pw)
    tips = []

    if not info["length_ok"]:
        tips.append("Use at least 8 characters.")
    if not info["has_upper"]:
        tips.append("Add an UPPERCASE letter (A–Z).")
    if not info["has_lower"]:
        tips.append("Add a lowercase letter (a–z).")
    if not info["has_digit"]:
        tips.append("Add a digit (0–9).")
    if not info["has_symbol"]:
        tips.append("Add a symbol from !@#$%^&*+-.")
    return tips

def generate_password(length):
    import random
    if length < 8:
        print("Info: Enforcing minimum length 8.")
        length = 8

    pw = ""
    pw += random.choice(UPPERS)
    pw += random.choice(LOWERS)
    pw += random.choice(DIGITS)
    pw += random.choice(SYMBOLS)

    all_chars = UPPERS + LOWERS + DIGITS + SYMBOLS
    while len(pw) < length:
        pw += random.choice(all_chars)

    pw_list = list(pw)
    random.shuffle(pw_list)
    final_pw = ""
    for ch in pw_list:
        final_pw += ch

    return final_pw

def print_strength_report(pw, report):
    def mark(ok):
        if ok:
            return "✔"
        else:
            return "✘"

    print("\nPassword Strength Report")
    print("------------------------")
    print("Length ≥ 8                 :", mark(report["length_ok"]), "(len=" + str(len(pw)) + ")")
    print("Has UPPERCASE [A–Z]        :", mark(report["has_upper"]))
    print("Has lowercase [a–z]        :", mark(report["has_lower"]))
    print("Has digit [0–9]            :", mark(report["has_digit"]))
    print("Has symbol [!@#$%^&*+-]    :", mark(report["has_symbol"]))
    if report["all_ok"]:
        print("Overall                    : STRONG ✅")
    else:
        print("Overall                    : WEAK ❌")

def main():
    while True:
        print("""
Password Assistant
------------------
1) Check a password
2) Generate a strong password
3) Quit
""")
        choice = input("Choice: ")

        if choice == "1":
            pw = input("Enter password: ")
            result = check_strength(pw)
            print_strength_report(pw, result)
            if not result["all_ok"]:
                tips = suggestions_for(pw)
                if len(tips) > 0:
                    print("\nSuggestions:")
                    for t in tips:
                        print("-", t)

        elif choice == "2":
            length_text = input("Desired length (>=8, default 12): ")
            if length_text.isdigit():
                length = int(length_text)
            else:
                length = 12
            pw = generate_password(length)
            print("\nGenerated:", pw)
            result = check_strength(pw)
            print_strength_report(pw, result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()