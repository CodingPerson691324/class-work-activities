import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(1000,1100)
polygon = turtle.Turtle()
polygon.speed(0)
num_sides = 22
side_length = 70
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()