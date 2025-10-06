# Evaluate using conditional statement.
# a)check whether a given number is even or odd and return 'even' or 'odd' appropriately.
# b)check whether an item is available in a list and 'available' or 'not available' appropriately


n = int(input("Enter a number: "))
print("even" if n % 2 == 0 else "odd")


lst = [10, 20, 30, 40, 50]
item = int(input("Enter item to search: "))
print("available" if item in lst else "not available")


# Enter a number: 7
# odd
# Enter item to search: 30
# available
