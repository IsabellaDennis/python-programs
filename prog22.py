# Write a program to search an item in a given list and display the number of occurrences of the given item.
def count_item():
    lst = input("Enter list elements separated by space: ").split()
    item = input("Enter item to search: ")
    print("Occurrences of", item, ":", lst.count(item))
count_item()

# Example Output:
# Enter list elements separated by space: 2 3 4 2 2 5
# Enter item to search: 2
# Occurrences of 2 : 3

