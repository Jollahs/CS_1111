import turtle

window = turtle.Screen()

pirate = turtle.Turtle()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.right(angle)
    pirate.forward(100)

window.exitonclick()
