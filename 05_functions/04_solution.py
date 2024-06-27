# Create a function that returns both the area and circumference of a circle giver its radius.

import math
def circle_status(radius):
    area = math.pi * radius**2;
    circumference = 2 * math.pi * radius;
    return area, circumference;

area, circumference = circle_status(3)
print("Area: ", round(area, 2), "\nCircumference: ", round(circumference, 2))
print("Area : {:.2f}, \nCircumference : {:.2f} ".format(area, circumference));