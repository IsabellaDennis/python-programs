# Arrange characters in a string such that lowercase letters must come first.

s = input("Enter a string: ")

lower = "".join([ch for ch in s if ch.islower()])
upper = "".join([ch for ch in s if ch.isupper()])

print("Arranged string =", lower + upper)

# SAMPLE OUTPUT:
# Enter a string: HeLLoWorLD
# Arranged string = eoorHeLLWD
