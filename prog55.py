# Find the sum of even valued terms in a Fibonacci series.

limit = int(input("Enter how many Fibonacci terms: "))

a, b = 0, 1
total = 0

for _ in range(limit):
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("Sum =", total)

# SAMPLE OUTPUT:
# Enter how many Fibonacci terms: 10
# Sum = 44
