# Braeden Audlin turtle race

import turtle
import random

wn = turtle.Screen()  # making the screen
wn.bgcolor('lightblue')
wn.title('Turtle Race Game')  # cool title command I found online
finishlinex = 250 # apparently this is the easiest way to do this for determining winner

lance = turtle.Turtle()
andy = turtle.Turtle()
john = turtle.Turtle()
james = turtle.Turtle()
line = turtle.Turtle()

line.hideturtle()  # making the line invisible

lance.color('red')  # turtle shapes and color
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
john.color('pink')
james.color('purple')
john.shape('turtle')
james.shape('turtle')
line.shape('turtle')

andy.penup()  # making sure they don't make lines
lance.penup()
john.penup()
james.penup()
line.penup()

andy.goto(-250, 50)  # starting positions
lance.goto(-250, -50)
john.goto(-250, 0)
james.goto(-250, 100)
line.goto(250, 250)

line.pendown()  # making a line
line.goto(250, -250)

while True:

    speed = random.randint(2, 8)
    lance.forward(speed)
    if lance.pos()[0] >= 250:  # not sure why I needed to add the [] after () but a debugger said I did, still a little unsure on what it does.
        lance.write("I won the race!")
        break

    speed = random.randint(2, 8)
    andy.forward(speed)
    if andy.pos()[0] >= 250:
        andy.write("I won the race!")
        break

    speed = random.randint(2, 8)
    john.forward(speed)
    if john.pos()[0] >= 250:
        john.write("I won the race!")
        break

    speed = random.randint(2, 8)
    james.forward(speed)
    if james.pos()[0] >= 250:
        james.write("I won the race!")
        break

wn.exitonclick()
