import re
import argparse

COMMON_PASSWORDS = ["password123", "12345678", "ledgerpro123", "qwerty123"]

def check_password_policy(password):
    errors = []
    if len(password) < 12:
        errors.append("Password must be at least 12 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("Must have 1 uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("Must have 1 lowercase letter")
    if not re.search(r"[0-9]", password):
        errors.append("Must have 1 number")
    if not re.search(r"[!@#$%^&*]", password):
        errors.append("Must have 1 special char (!@#$%^&*)")
    if "ledgerpro" in password.lower():
        errors.append("Must NOT contain 'LedgerPro'")
    if password.lower() in COMMON_PASSWORDS:
        errors.append("Too common password")
    return len(errors) == 0, errors

def run_tests():
    print("--- LedgerPro Accountants - Test Run ---")
    samples = [
        ("ali.ahmed@ledgerpro.pk", "Audit2025!Secure"),
        ("sara.khan@ledgerpro.pk", "ledgerpro123"),
        ("finance@ledgerpro.pk", "Tax@2025-Lahore"),
    ]
    for email, pwd in samples:
        ok, errs = check_password_policy(pwd)
        result = "PASS" if ok else "FAIL: " + ", ".join(errs)
        print(f"{email} | {pwd} => {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run test')
    args = parser.parse_args()
    if args.test:
        run_tests()
    else:
        pwd = input("Enter password to check: ")
        ok, errs = check_password_policy(pwd)
        if ok:
            print("Password is VALID for LedgerPro policy.")
        else:
            print("Password INVALID:")
            for e in errs:
                print(f" - {e}")
