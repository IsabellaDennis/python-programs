# List Comprehension:
# (a) Generate positive list of numbers from a given list of numbers
# (b) Generate a list with square of numbers from a given list
# (c) Form a list containing vowels from a given word
# (d) Generate a list of numbers by removing even numbers from a given list
# (e) Display leap years from current year to a future year entered by user


nums = [-1,2,-3,4,5]
print([x for x in nums if x > 0])               # a
print([x*x for x in nums])                      # b
print([x for x in "python" if x in 'aeiou'])    # c
print([x for x in nums if x % 2 != 0])          # d

start, end = 2020, 2030
print([y for y in range(start, end+1) if y%4==0 and (y%100!=0 or y%400==0)]) # f




# [2, 4, 5]
# [1, 4, 9, 16, 25]
# ['o']
# [-1, -3, 5]
# [2020, 2024, 2028]