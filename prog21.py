# Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.
def join_digits():
    digits = input("Enter single-digit numbers separated by space: ").split()
    print("Concatenated number:", ''.join(digits))
join_digits()

# Example Output:
# Enter single-digit numbers separated by space: 1 5 7 9
# Concatenated number: 1579

