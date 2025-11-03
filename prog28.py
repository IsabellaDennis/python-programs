# Question 9:
# Write lambda functions:
# (a) To find largest of 2 numbers
# (b) To check if number is divisible by 5
# (c) To remove all strings with length <5 from list
# (d) To increment integers by 10% if >1000 else by 5%


# (a) To find largest of 2 numbers
largest = lambda a, b: a if a > b else b
print("Largest number:", largest(10, 25))


# (b) To check if number is divisible by 5
divisible_by_5 = lambda x: "yes" if x % 5 == 0 else "no"
print("25 is divisible by 5?", divisible_by_5(25))
print("22 is divisible by 5?", divisible_by_5(22))


# (c) To remove all strings with length <5 from list
strings = ["apple", "cat", "banana", "dog", "grapes"]
filtered = list(filter(lambda s: len(s) >= 5, strings))
print("Strings with length ≥ 5:", filtered)


# (d) To increment integers by 10% if >1000 else by 5%
numbers = [500, 1200, 800, 2000]
incremented = list(map(lambda n: n + n * 0.10 if n > 1000 else n + n * 0.05, numbers))
print("Incremented list:", incremented)


# ------------------ OUTPUT ------------------
# Largest number: 25
# 25 is divisible by 5? yes
# 22 is divisible by 5? no
# Strings with length ≥ 5: ['apple', 'banana', 'grapes']
# Incremented list: [525.0, 1320.0, 840.0, 2200.0]
