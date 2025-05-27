# Author: Tega Omarejedje
# Assignment: Password Strength Checker
# Date: 05/27/2025

import string

# Step 1: Input the Password
userpassword = input("Enter a password: ")

# Step 2: Evaluate the Password
messages = []
score = 0

# Length check
if len(userpassword) >= 8:
    score += 2
else:
    messages.append("Your password needs to be at least 8 characters long.")

# Uppercase check
if any(char.isupper() for char in userpassword):
    score += 2
else:
    messages.append("Your password needs at least one uppercase letter.")

# Lowercase check
if any(char.islower() for char in userpassword):
    score += 2
else:
    messages.append("Your password needs at least one lowercase letter.")

# Digit check
if any(char.isdigit() for char in userpassword):
    score += 2
else:
    messages.append("Your password needs at least one digit.")

# Special character check
special_chars = string.punctuation
if any(char in special_chars for char in userpassword):
    score += 2
else:
    messages.append("Your password needs at least one special character (e.g. @, #, $).")

# Output results
if score == 10:
    print("Your password is strong! 💪")
else:
    print("Password check results:")
    for msg in messages:
        print("- " + msg)

# Bonus: Password strength meter
print(f"Password Strength Score: {score}/10")
