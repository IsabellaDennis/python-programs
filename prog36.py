# Find the longest word in the file

filename = input("Enter file name: ")

f = open(filename, 'r')
words = f.read().split()
f.close()

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length:", len(longest))


# Enter file name: sample.txt
# Longest word: programming
# Length: 11


