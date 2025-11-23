# Create Person(name, roll) and Marks(Maths, Computer).
# Create Student(Person, Marks) → Display details and pass/fail (50% needed).

class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self, maths, computer):
        self.maths = maths
        self.computer = computer

class Student(Person, Marks):
    def __init__(self, name, roll, maths, computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, computer)

    def display(self):
        total = self.maths + self.computer
        percent = total / 2
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Percentage:", percent)
        print("Status:", "PASS" if percent >= 50 else "FAIL")

s = Student("Bella", 101, 60, 75)
s.display()

# OUTPUT:
# Name: Bella
# Roll: 101
# Percentage: 67.5
# Status: PASS
