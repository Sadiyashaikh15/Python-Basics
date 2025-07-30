import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Taking input from user
r = float(input("Enter the radius of the circle: "))

# Creating object of Circle
circle1 = Circle(r)

# Displaying results
print(f"Area of the circle = {circle1.area():.2f}")
print(f"Perimeter (Circumference) of the circle = {circle1.perimeter():.2f}")
