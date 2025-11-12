'''Create class Engine (_power) and Wheels (size).
 Derive the class Car (model) from Engine & Wheels.
 Display details of the car using method overriding'''

class Engine:
    def __init__(self, _power):
        self._power = _power

    def display(self):
        print("Engine Power:", self._power, "HP")


class Wheels:
    def __init__(self, _size):
        self._size = _size

    def display(self):
        print("Wheel Size:", self._size, "inches")


class Car(Engine, Wheels):
    def __init__(self, _power, _size, _model):
        Engine.__init__(self, _power)
        Wheels.__init__(self, _size)
        self._model = _model

    def display(self):
        print("Car Model:", self._model)
        Engine.display(self)
        Wheels.display(self)


# Create object
c1 = Car(120, 16, "Hyundai i20")

# Display details
c1.display()

# ------------------------------------------------------
# OUTPUT:
# Car Model: Hyundai i20
# Engine Power: 120 HP
# Wheel Size: 16 inches
# ------------------------------------------------------
