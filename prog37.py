#Write a Python program to remove all lines starting with '#' (comments) from a file.

filename = input("Enter file name: ")

try:
    f = open(filename, 'r')
    data = f.readlines()
    f.close()

    f = open(filename, 'w')
    for line in data:
        if not line.strip().startswith("#"):
            f.write(line)
    f.close()
    print("Comments removed successfully.")

except FileNotFoundError:
    print("File not found.")