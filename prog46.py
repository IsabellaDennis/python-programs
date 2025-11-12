# Create class Currency(amount, unit).
# Overload '==' operator to check if two currencies are equal.


class Currency:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit


# Create objects
c1 = Currency(100, "INR")
c2 = Currency(100, "INR")
c3 = Currency(200, "USD")

# Compare
print(c1 == c2)  # True
print(c1 == c3)  # False

# ------------------------------------------------------
# OUTPUT:
# True
# False
# ------------------------------------------------------
