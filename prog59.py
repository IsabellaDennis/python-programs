# Function nearly_equal:
# Two strings are nearly equal if they differ by exactly 1 character.

a = input("Enter first string: ")
b = input("Enter second string: ")

if len(a) != len(b):
    print("Not nearly equal")
else:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1

    print("Nearly equal" if diff == 1 else "Not nearly equal")

# SAMPLE OUTPUT:
# Enter first string: hello
# Enter second string: hallo
# Nearly equal
