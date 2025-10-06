# accept a list of numbers from user create a new list with number greats than 100 from the input list using comprehension





nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
new_list = [x for x in nums if x > 100]
print("Numbers greater than 100:", new_list)



# Enter numbers separated by spaces: 50 120 200 90 150
# Numbers greater than 100: [120, 200, 150]

