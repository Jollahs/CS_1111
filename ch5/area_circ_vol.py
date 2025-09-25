import math

radius = float(input("Radius? "))

# pi = math.pi

# compute the area
area = math.pi * math.pow(radius, 2)
circumference = 2 * radius * math.pi
volume = 4 / 3 * math.pi * math.pow(radius, 3)

print("Area: ", area, "units squared")
print("Circumference: ", circumference, "units")
print("Volume: ", volume, "units cubed")
