# Write a program that computes and prints a random x-coordinate
# and y-coordinate in the range [0,1)

# Your program should
# Use sqrt from the math module
# Use the pow function from the math module
# Use a variable to define all four coordinates in the problem

import math
import random

TARGET_X = 0.5
TARGET_Y = 0.5

xcoord = random.random()
ycoord = random.random()

print("(" + str(xcoord) + ", " + str(ycoord) + ")")

# Then calculate and print the distance of this coordinate from the point (0.5, 0.5)
distance = math.sqrt(math.pow(xcoord - TARGET_X, 2) + math.pow(ycoord - TARGET_Y, 2))

print("Distance from target is: ", distance)

