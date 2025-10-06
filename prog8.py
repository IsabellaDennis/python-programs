# find the longest word from a comma seperated list entered by user





words = input("Enter words separated by commas: ").split(',')

longest = max(words, key=len)
print("Longest word:", longest)


# Enter words separated by commas: apple,banana,kiwi,strawberry
# Longest word: strawberry

