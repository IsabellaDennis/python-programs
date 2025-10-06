# Write a program to get a string from the user
# (a) Replace all occurrences of the first character with ‘$’, except the first character
# (b) Create a string from given string where first and last characters are exchanged



s = input("Enter a string: ")
print(s[0] + s[1:].replace(s[0], '$'))

s = input("Enter a string: ")
print(s[-1] + s[1:-1] + s[0])




# Enter a string: babble
# ba$$le

# Enter a string: python
# nythop