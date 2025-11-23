# Compare above 2 students based on pass percentage.

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


# Compare above 2 students based on pass percentage.

def compare(s1, s2):
    p1 = (s1.maths + s1.computer) / 2
    p2 = (s2.maths + s2.computer) / 2

    if p1 > p2:
        print("Student 1 has higher percentage")
    elif p2 > p1:
        print("Student 2 has higher percentage")
    else:
        print("Both have equal percentage")


# creating 2 students
s1 = Student("A", 1, 60, 70)
s2 = Student("B", 2, 80, 50)

compare(s1, s2)

# OUTPUT:
# Both have equal percentage

