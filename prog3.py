# Write a program to
# (a) Print out all colours from color-list1 not contained in color-list2
# (b) Write a program to remove duplicates from a list
# (c) Write a program to check whether a list is empty or not


c1 = ["red", "green", "blue"]
c2 = ["yellow", "green", "pink"]
print([x for x in c1 if x not in c2])

lst = [1, 2, 2, 3, 4, 4]
print(list(set(lst)))

lst = []
print("empty" if not lst else "not empty")



# ['red', 'blue']
# [1, 2, 3, 4]
# empty
