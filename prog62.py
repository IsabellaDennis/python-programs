# Print Armstrong numbers in the range (100, 500).

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for n in range(start, end+1):
    s = str(n)
    if sum(int(d)**3 for d in s) == n:
        print(n)

# SAMPLE OUTPUT:
# Enter start: 100
# Enter end: 500
# 153
# 370
# 371
# 407
