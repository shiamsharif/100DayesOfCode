from turtle import Turtle, Screen

the_turtle = Turtle()
screen = Screen()

def move_forward():
    the_turtle.forward(10)

def move_backward():
    the_turtle.backward(10)

def go_right():
    new_heading = the_turtle.heading() - 10
    the_turtle.setheading(new_heading)


def go_left():
    new_heading = the_turtle.heading() + 10
    the_turtle.setheading(new_heading)

def clear():
    the_turtle.clear()
    the_turtle.penup()
    the_turtle.home()
    the_turtle.pendown()
    

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()