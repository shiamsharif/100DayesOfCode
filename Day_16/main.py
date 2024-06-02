from turtle import Turtle, Screen

a = Turtle()
print(a)
for z in range(0,3):
    a.shape("turtle")
    a.color("purple")
    a.forward(100)
    a.forward(100)
    a.left(120)
    a.forward(100)
    a.forward(100)
    a.left(120)
    a.forward(100)
    a.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()