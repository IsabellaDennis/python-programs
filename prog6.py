# write a python fuction that takes a list and returns a new list with unique elements of the first list




nums = list(map(int, input("Enter numbers: ").split()))
print(list(set(nums)))


# Enter numbers: 1 2 2 3 4 4 5
# [1, 2, 3, 4, 5]
