from graphics import rectangle, circle
from graphics.threeD_graphics import cuboid, sphere

print("Rectangle area:", rectangle.area(5, 3))
print("Rectangle perimeter:", rectangle.perimeter(5, 3))

print("Circle area:", circle.area(4))
print("Circle perimeter:", circle.perimeter(4))

print("Cuboid area:", cuboid.area(4, 3, 2))
print("Cuboid perimeter:", cuboid.perimeter(4, 3, 2))

print("Sphere area:", sphere.area(3))
print("Sphere perimeter:", sphere.perimeter(3))