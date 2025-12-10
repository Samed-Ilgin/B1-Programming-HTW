import string
import random

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_special_char(password):
    special = "!@#$%^&*"
    for char in password:
        if char in special:
            return True
    return False

def validate_password(password):
    results = {
        "min_length": check_min_length(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "digit": has_digit(password),
        "special_char": has_special_char(password)
    }
    results["is_valid"] = all(results.values())

    return results


success_messages = [ "Great job!", "Nice!", "Perfect!"]

fail_messages = ["Keep trying!", "Almost there!", "Needs improvement!",]

password = input("Enter a password to test: ")

results = validate_password(password)

print("\nPassword Check Results\n")

if results["min_length"]:
    print("Minimum length met")
else:
    print("Minimum length NOT met")

if results["uppercase"]:
    print("Has uppercase letter")
else:
    print("Missing uppercase letter")

if results["lowercase"]:
    print("Has lowercase letter")
else:
    print("Missing lowercase letter")

if results["digit"]:
    print("Has a number")
else:
    print("Missing a number")

if results["special_char"]:
    print("Has special character")
else:
    print("Missing special character")


print("\nPassword is:", "VALID " if results["is_valid"] else "NOT VALID ")


if results["is_valid"]:
    print("Password Strength: STRONG")
    print(random.choice(success_messages))
else:
    print("Password Strength: WEAK")
    print(random.choice(fail_messages))