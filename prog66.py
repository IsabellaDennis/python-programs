# Display alternate characters from a line of text using recursion.

def alternate(text, i=0):
    if i >= len(text):
        return ""
    return text[i] + alternate(text, i+2)

result = alternate("computer")

print(result)

# OUTPUT:
# cmue
