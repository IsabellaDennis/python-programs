# Find the lengthiest line in the file

filename = input("Enter file name: ")

f = open(filename, 'r')
lines = f.readlines()
f.close()

longest_line = ""
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line

print("The lengthiest line is:")
print(longest_line)
print("Length of the line:", len(longest_line))


# Enter file name: sample.txt
# The lengthiest line is:
# Python is amazing
# Length of the line: 19

