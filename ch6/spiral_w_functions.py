import turtle

def draw_square(_a, side_length):
    for side in range(4):
        _a.forward(side_length)
        _a.left(90)

def draw_spiral(_a, _radius):
    """Use turtle a to draw spiral of squares with radius radius"""
    for i in range(36): # repeat
        draw_square(_a, _radius)
        # rotate 10 before next square
        _a.left(10) # rotate turtle


window = turtle.Screen()

a = turtle.Turtle()
a.speed(0)

radius = 100

draw_spiral(a, radius)
draw_spiral(a, radius*2)

window.exitonclick()
