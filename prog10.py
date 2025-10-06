# Write a program to
# (a) Determine frequency of alphabets in a word
# (b) Create a list of first-names. Count the number of names that starts with ‘a’
# (c) Each word in a line of text


word = input("Enter word: ")
for i in set(word):
    print(i, "=", word.count(i))


names = ["anu", "arya", "alex", "binoy", "adam"]
print(sum(n.startswith('a') for n in names))


txt = input("Enter a line: ").split()
print(len(txt))




# Enter word: apple
# a = 1
# p = 2
# l = 1
# e = 1
# 3
# Enter a line: this is python
# 3