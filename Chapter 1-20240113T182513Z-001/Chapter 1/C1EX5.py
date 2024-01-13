import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
print(f"{area_of_circle(radius):.2f}.")