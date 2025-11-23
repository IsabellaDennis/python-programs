# Create class Book (title, author). Add attribute 'publisher' at runtime.
# If publisher exists print: "<title> written by <author> is published by <publisher>"
# Else print: "Unknown Publisher"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("Python Basics", "John Mathew")
b.publisher = "Oxford Press"  # added at runtime

if hasattr(b, "publisher"):
    print(f"{b.title} written by {b.author} is published by {b.publisher}")
else:
    print("Unknown Publisher")

# OUTPUT:
# Python Basics written by John Mathew is published by Oxford Press
