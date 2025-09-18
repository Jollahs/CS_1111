# Use for loops to draw polygons

import turtle

# create the window
window = turtle.Screen()

shape_drawer = turtle.Turtle()
shape_drawer.shape("turtle")

num_sides = 6

# for side in [0,1,2,3,4]:
for side in range(num_sides):
    shape_drawer.forward(100)
    shape_drawer.left(360/num_sides)

# 120 for 3 sides
# 90 for 4 sides
# ? for 5 sides

window.exitonclick()
