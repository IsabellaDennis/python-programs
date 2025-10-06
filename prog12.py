# Write python program to add ‘ing’ at the end of the string. If already ends with ‘ing’, then add ‘ly’.


s = input("Enter a word: ")
print(s + 'ly' if s.endswith('ing') else s + 'ing')



# Enter a word: play
# playing

# Enter a word: running
# runningly