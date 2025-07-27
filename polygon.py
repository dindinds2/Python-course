import turtle
turtle.Screen().bgcolor("White")
turtle.Screen().setup(500,300)
polygon = turtle.Turtle()
num_sides = 6
sides_length = 70
angle = 360.0/num_sides
for i in range(num_sides):
    polygon.forward(sides_length)
    polygon.right(angle)
turtle.done()