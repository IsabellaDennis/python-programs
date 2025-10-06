# write a program to generate all factors of a given number





num = int(input("Enter a number: "))

factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors of", num, "are:", factors)



# Enter a number: 12
# Factors of 12 are: [1, 2, 3, 4, 6, 12]

