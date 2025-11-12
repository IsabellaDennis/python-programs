# Create class Person with private attributes name and age.
# Compare 2 Persons by their age

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __lt__(self, other):
        return self.__age < other.__age


# Create objects
p1 = Person("Anu", 25)
p2 = Person("Binu", 30)

print(p1 < p2)  # True if Anu is younger

# ------------------------------------------------------
# OUTPUT:
# True
# ------------------------------------------------------

