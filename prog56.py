# Given a string of odd length greater than 7,
# return a new string made of the middle three characters of a given string.

s = input("Enter a string: ")

# Check conditions
if len(s) > 7 and len(s) % 2 == 1:
    mid = len(s) // 2
    result = s[mid-1 : mid+2]
    print("Middle three characters:", result)
else:
    print("Invalid input (string must be odd length and greater than 7)")

# SAMPLE OUTPUT:
# Enter a string: computer
# Middle three characters: put

