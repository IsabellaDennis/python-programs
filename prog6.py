# write a python fuction that takes a list and returns a new list with unique elements of the first list




def unique_words_list(words):
    unique_words = []
    [unique_words.append(word) for word in words if word not in unique_words]
    return unique_words

words = input("Enter words separated by space: ").split()
print("Unique words:", unique_words_list(words))





# Enter words separated by space: apple banana apple mango banana
# Unique words: ['apple', 'banana', 'mango']
