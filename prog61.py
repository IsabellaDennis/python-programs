# Compare two lists entered by user.

l1 = input("Enter list 1 elements (space separated): ").split()
l2 = input("Enter list 2 elements (space separated): ").split()

print("Lists are equal" if l1 == l2 else "Lists are not equal")

# SAMPLE OUTPUT:
# Enter list 1: 1 2 3
# Enter list 2: 1 2 3
# Lists are equal
