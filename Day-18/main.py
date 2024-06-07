"""######## Challenge 1 - Draw a Square ############"""

from turtle import Screen, Turtle

the_turtle = Turtle()


# for _ in range(4):
#     the_turtle.forward(100)
#     the_turtle.right(90)




"""#######Challenge 2 - Draw a Dashed Line ########"""

## From stackOverFlow
# for _ in range(15):
#     the_turtle.forward(10)
#     the_turtle.color("white")
#     the_turtle.forward(10)
#     the_turtle.color("black")


# # From Angela Yo
# for _ in range(15):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()




"""########### Challenge 3 - Draw Shapes ########"""

"""My solution"""

# # Triangle:
# the_turtle.color("blue")
# for _ in range(3):
#     the_turtle.forward(100)
#     the_turtle.right(120)

# # Square:
# the_turtle.color("purple")
# for _ in range(4):
#     the_turtle.forward(100)
#     the_turtle.right(90)

# # Pentagon:
# the_turtle.color("orange")
# for _ in range(5):
#     the_turtle.forward(100)
#     the_turtle.right(72)

# # Hexagon:
# the_turtle.color("green")
# for _ in range(6):
#     the_turtle.forward(100)
#     the_turtle.right(60)

# # Heptagon:
# the_turtle.color("red")
# for _ in range(7):
#     the_turtle.forward(100)
#     the_turtle.right(51.42)

# # Octatagon:
# the_turtle.color("cyan")
# for _ in range(8):
#     the_turtle.forward(100)
#     the_turtle.right(45)

# # Nonagon:
# the_turtle.color("yellow")
# for _ in range(9):
#     the_turtle.forward(100)
#     the_turtle.right(40)

# # Decaagon:
# the_turtle.color("pink")
# for _ in range(10):
#     the_turtle.forward(100)
#     the_turtle.right(36)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        the_turtle.forward(100)
        the_turtle.right(angle)


for shape_side_n in range(3,11):
    draw_shape(shape_side_n)



 






screen = Screen()
screen.exitonclick()