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

# Example Output:
# Enter file name: sample.txt
# Longest word: programming
