# Accept percentage of marks from user and display the grade


p = float(input("Enter percentage: "))
if p >= 90: print("Grade: A+")
elif p >= 80: print("Grade: A")
elif p >= 70: print("Grade: B")
elif p >= 60: print("Grade: C")
elif p >= 50: print("Grade: D")
else: print("Grade: F")


# Enter percentage: 85
# Grade: A
# Enter percentage: 45
# Grade: F
