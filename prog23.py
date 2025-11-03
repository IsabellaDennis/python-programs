# Write a program to print all even numbers from a given list in order until you reach 237 or end of list.
def even_until_237():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Even numbers until 237:")
    for n in lst:
        if n == 237:
            break
        if n % 2 == 0:
            print(n, end=' ')
    print()
even_until_237()

# Example Output:
# Enter numbers separated by space: 10 23 34 50 237 12
# Even numbers until 237:
# 10 34 50

