# Remove a line from a specific position in a file

filename = input("Enter file name: ")
pos = int(input("Enter line number to remove: "))

f = open(filename, 'r')
lines = f.readlines()
f.close()

f = open(filename, 'w')
for i in range(len(lines)):
    if i != pos - 1:
        f.write(lines[i])
f.close()
print("Line removed successfully!")

# Example Output:
# Enter file name: sample.txt
# Enter line number to remove: 3
# Line removed successfully!

