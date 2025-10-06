# Write a program to
# (a) Write a program to check if a given key already exists in a dictionary
# (b) Write python program to merge two dictionaries
# (c) Write a program to sort a dictionary in ascending and descending order
# (d) Write a program to create an inverted dictionary


d = {'a':1, 'b':2}
k = input("Enter key: ")
print("Exists" if k in d else "Not exists")


d1 = {'a':1, 'b':2}
d2 = {'c':3}
d1.update(d2)
print(d1)


d = {'b':2, 'a':1, 'c':3}
print(dict(sorted(d.items())))       # ascending
print(dict(sorted(d.items(), reverse=True)))  # descending


d = {'a':1, 'b':2}
print({v:k for k,v in d.items()})




# Enter key: a
# Exists
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3}
# {'c': 3, 'b': 2, 'a': 1}
# {1: 'a', 2: 'b'}