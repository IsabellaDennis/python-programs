# a)find the factorial of a number
# b)find the fibonacci series and find nth number
# c)find the sum of elements in a list and find the position of that number


# a
n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)


# b
n = int(input("Enter n: "))

a, b = 0, 1
series = []

for i in range(n):
    series.append(a)
    a, b = b, a + b

print("Fibonacci series:", series)
print(f"{n}th Fibonacci number:", series[-1])


# c
nums = list(map(int, input("Enter numbers: ").split()))
print("Sum of elements:", sum(nums))
num = int(input("Enter element to find: "))
pos = [i+1 for i in range(len(nums)) if nums[i] == num]
print(f"Element {num} found at position(s): {pos}" if pos else f"Element {num} not found")







# Enter a number: 5
# Factorial: 120

# Enter n: 7
# Fibonacci series: [0, 1, 1, 2, 3, 5, 8]
# 7th Fibonacci number: 8

# Enter numbers: 2 3 5 3 7
# Sum of elements: 20
# Enter element to find: 3
# Element 3 found at position(s): [2, 4]
