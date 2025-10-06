# Accept a string and return the length of longest word.If the result has more than one word,then print 'BINGO'



s = input("Enter a string: ").split()
longest = max(len(word) for word in s)
if sum(len(word) == longest for word in s) > 1:
    print("BINGO")
else:
    print(longest)


# Enter a string: hello world python
# BINGO
# Enter a string: beautiful code
# 9


