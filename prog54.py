# Check whether a given positive integer is power of 2.
# Raise exception for negative input.

n = int(input("Enter a number: "))

try:
    if n < 0:
        raise Exception("Negative number not allowed")

    if (n & (n-1)) == 0:
        print("Power of 2")
    else:
        print("Not power of 2")

except Exception as e:
    print(e)

# SAMPLE OUTPUT:
# Enter a number: 8
# Power of 2

