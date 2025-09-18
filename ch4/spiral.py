import turtle

window = turtle.Screen()

a = turtle.Turtle()
a.speed(9)
for i in range(36):
    # draw a square
    for side in range(4):
        a.forward(100)
        a.left(90)
    # rotate 10 before next square
    a.left(10)

window.exitonclick()
