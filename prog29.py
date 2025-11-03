# Write lambda functions, each to find the area of square, rectangle and triangle

# Lambda functions to find area

square_area = lambda side: side * side
rectangle_area = lambda length, breadth: length * breadth
triangle_area = lambda base, height: 0.5 * base * height

# Example usage
print("Area of square:", square_area(4))
print("Area of rectangle:", rectangle_area(5, 3))
print("Area of triangle:", triangle_area(6, 4))



# Area of square: 16
# Area of rectangle: 15
# Area of triangle: 12.0
