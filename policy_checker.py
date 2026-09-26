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
        errors.append("Must not contain 'ledgerpro'")
    if password in COMMON_PASSWORDS:
        errors.append("Password is too common")
    return len(errors) == 0, errors
