# Count number of lines in a file

filename = input("Enter file name: ")
f = open(filename, 'r')
lines = f.readlines()
f.close()
print("Number of lines:", len(lines))

# Example Output:
# Enter file name: sample.txt
# Number of lines: 5
