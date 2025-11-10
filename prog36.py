# Remove comments from a file (lines starting with #)

filename = input("Enter file name: ")
f = open(filename, 'r')
lines = f.readlines()
f.close()

f = open(filename, 'w')
for line in lines:
    if not line.strip().startswith("#"):
        f.write(line)
f.close()
print("Comments removed successfully!")

# Example Output:
# Enter file name: sample.txt
# Comments removed successfully!

