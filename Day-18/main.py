######## Challenge 1 - Draw a Square ############

from turtle import Screen, Turtle

the_turtle = Turtle()


for _ in range(4):
    the_turtle.forward(100)
    the_turtle.right(90)


screen = Screen()
screen.exitonclick()