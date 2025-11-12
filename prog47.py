'''Create a class FruitBasket (fruit_name, price per kg).
 Overload '+' operator that adds two fruit baskets with unique fruits having least price from 2 baskets.'''


class FruitBasket:
    def __init__(self, fruit_name, price_per_kg):
        self.fruits = {fruit_name: price_per_kg}

    def __add__(self, other):
        result = self.fruits.copy()
        for fruit, price in other.fruits.items():
            if fruit in result:
                result[fruit] = min(result[fruit], price)
            else:
                result[fruit] = price
        new_basket = FruitBasket("", 0)
        new_basket.fruits = result
        return new_basket

    def display(self):
        for fruit, price in self.fruits.items():
            print(fruit, ":", price, "per kg")


# Create baskets
b1 = FruitBasket("Apple", 120)
b2 = FruitBasket("Orange", 80)
b3 = FruitBasket("Apple", 100)

# Combine
b4 = b1 + b2 + b3
b4.display()

# ------------------------------------------------------
# OUTPUT:
# Apple : 100 per kg
# Orange : 80 per kg
# ------------------------------------------------------
