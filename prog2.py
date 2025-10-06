# Write a program to
# (a) Create a single string separated with space from two strings by swapping the character at position 1
# (b) Create a list of colours from a comma-separated list of colour names entered by the user. Print alternate colours

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s2[0]+s1[1:], s1[0]+s2[1:])

colors = input("Enter colors separated by commas: ").split(',')
print(colors[::2])




# Enter first string: abc
# Enter second string: xyz
# xbc ayz

# Enter colors separated by commas: red,blue,green,yellow,black
# ['red', 'green', 'black']