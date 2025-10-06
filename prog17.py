# Generate a string by combining first two characters and last two characters from an input string
# If length of input string is 2,then resultant string must be a concatenation of those characters or if length is less than 2,return an empty string instead.


s = input("Enter a string: ")
print(s[:2] + s[-2:] if len(s) > 2 else (s*2 if len(s) == 2 else ""))

# Enter a string: python
# pyon

# Enter a string: go
# gogo

# Enter a string: a
# (empty)
