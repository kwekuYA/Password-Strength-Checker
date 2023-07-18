# Importing relevant modules
import re

def check_password_strength(password):
    errors = []

    # Minimum length requirement
    if len(password) < 8:
        errors.append("Password is too short. It should be at least 8 characters long.")

    # Regular expressions to check for different types of characters
    regex_lowercase = re.compile(r'[a-z]')
    regex_uppercase = re.compile(r'[A-Z]')
    regex_digit = re.compile(r'\d')
    regex_special = re.compile(r'[^a-zA-Z\d\s]')

    # Check for lowercase letters
    if not regex_lowercase.search(password):
        errors.append("Password should contain at least one lowercase letter.")

    # Check for uppercase letters
    if not regex_uppercase.search(password):
        errors.append("Password should contain at least one uppercase letter.")

    # Check for digits
    if not regex_digit.search(password):
        errors.append("Password should contain at least one digit.")

    # Check for special characters
    if not regex_special.search(password):
        errors.append("Password should contain at least one special character.")

    if errors:
        return errors
    else:
        return "Password is strong."


password = input("Enter a password: ")
result = check_password_strength(password)

if isinstance(result, list):
    print("Password strength check failed. The following errors were found:")
    for error in result:
        print("- " + error)
else:
    print(result)
