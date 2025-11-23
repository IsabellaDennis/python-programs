# Create class Flower(name). Add attribute petalColor at runtime.
# If flower has petalColor print "<petalColor> <name>"
# else print "Unknown Flower".

class Flower:
    def __init__(self, name):
        self.name = name

name = input("Enter flower name: ")
f = Flower(name)

color = input("Enter petal color (leave blank if none): ")

if color.strip() != "":
    f.petalColor = color

if hasattr(f, "petalColor"):
    print(f"{f.petalColor} {f.name}")
else:
    print("Unknown Flower")

# SAMPLE OUTPUT:
# Enter flower name: Rose
# Enter petal color: Red
# Red Rose
