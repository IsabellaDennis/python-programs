# compare two lists entered by user



list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))


if list1 == list2:
    print("Both lists are equal")
else:
    print("Lists are not equal")



# Enter elements of first list: 1 2 3 4
# Enter elements of second list: 1 2 3 4
# Both lists are equal

