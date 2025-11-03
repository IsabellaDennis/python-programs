# Accept full name and display in reverse order with space between the words.
def reverse_name():
    name = input("Enter your full name: ")
    print("Reversed order:", ' '.join(name.split()[::-1]))
reverse_name()

# Example Output:
# Enter your full name: Bella Dennis
# Reversed order: Dennis Bella

