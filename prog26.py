# Write a program that counts odd and even numbers in a given list.
def count_odd_even():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    odd = sum(1 for n in lst if n % 2 != 0)
    even = len(lst) - odd
    print("Odd numbers:", odd)
    print("Even numbers:", even)
count_odd_even()

# Example Output:
# Enter numbers separated by space: 1 2 3 4 5 6
# Odd numbers: 3
# Even numbers: 3

