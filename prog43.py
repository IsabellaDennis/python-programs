'''Create a class Publisher (name).
 Derive a class Book (title, author) from Publisher. 
 Derive a class Python (price, no_of_pages) from Book. 
 Write a program that displays information about a Python book. 
 Use base class constructor invocation and method overriding'''

class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("No. of Pages:", self.no_of_pages)


# Create object for Python book
p1 = Python("O'Reilly Publications", "Learning Python", "Mark Lutz", 850, 1200)

# Display book details
p1.display()

# -----------------------------------------------
# OUTPUT:
# Publisher Name: O'Reilly Publications
# Book Title: Learning Python
# Author: Mark Lutz
# Price: 850
# No. of Pages: 1200
# -----------------------------------------------
