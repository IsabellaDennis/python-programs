# Check validity of password input by users.
# Conditions:
# • At least 1 lowercase
# • At least 1 uppercase
# • At least 1 digit
# • At least 1 char from [$#@]
# • Min length 6
# • Max length 16

p = input("Enter password: ")

lower = upper = digit = special = False

if 6 <= len(p) <= 16:
    for ch in p:
        if ch.islower(): lower = True
        elif ch.isupper(): upper = True
        elif ch.isdigit(): digit = True
        elif ch in "$#@": special = True

if lower and upper and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")

# SAMPLE OUTPUT:
# Enter password: Abc@123
# Valid Password
