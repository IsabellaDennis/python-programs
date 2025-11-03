# Write a program that counts strings where length is 2 or more and first and last characters are same.
def count_strings():
    lst = input("Enter strings separated by space: ").split()
    count = sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])
    print("Count of matching strings:", count)
count_strings()

# Example Output:
# Enter strings separated by space: aba xyz aa x bbb
# Count of matching strings: 3

