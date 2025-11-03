# Write recursive functions to:
# (a) find the factorial of a number
# (b) find the nth Fibonacci number
# (c) find the sum of an integer list
# (d) find the sum of first N whole numbers
# (e) reverse a string

# (a) Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# (b) nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("5th Fibonacci number:", fibonacci(5))

# (c) Sum of an integer list
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
print("Sum of list [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))

# (d) Sum of first N whole numbers
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)
print("Sum of first 5 whole numbers:", sum_n(5))

# (e) Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print("Reversed string 'hello':", reverse_string("hello"))




# Factorial of 5: 120
# 5th Fibonacci number: 5
# Sum of list [1, 2, 3, 4, 5]: 15
# Sum of first 5 whole numbers: 15
# Reversed string 'hello': olleh





