# Write a program that retrieves all lines from a file having words starting with 's' and ending with 'e'

with open("sample.txt", "r") as f:
    for line in f:
        w = line.strip()
        if w.startswith("s") and w.endswith("e"):
            print(w)

# OUTPUT:
# safe
# snake
# stone
