# Write a function to get a new string from a given string by adding 'Is' to the beginning.
# If the string already begins with 'Is', return the input string unchanged.
def add_is():
    s = input("Enter a string: ")
    if s.startswith('Is'):
        print("Result:", s)
    else:
        print("Result:", 'Is' + s)
add_is()

# Example Output:
# Enter a string: Python
# Result: IsPython

