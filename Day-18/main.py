
from turtle import Screen, Turtle
import random

the_turtle = Turtle()


"""######## Challenge 1 - Draw a Square ############"""

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


"""Form Angela Yu"""
# colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black","Cyan", "Magenta", "Lime", "Teal", "Navy", "Maroon", "Olive", "Silver", "Gold", "Coral"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         the_turtle.forward(100)
#         the_turtle.right(angle)


# for shape_side_n in range(3,11):
#     the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)



"""########### Challenge 4 - Draw a Random Walk ########"""

# angle = [0, 90, 180,270]

# colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black","Cyan", "Magenta", "Lime", "Teal", "Navy", "Maroon", "Olive", "Silver", "Gold", "Coral"]

# the_turtle.pensize(15)
# for shape_side_n in range (200):
#     the_turtle.color(random.choice(colors))
#     the_turtle.forward(30)
#     the_turtle.right(random.choice(angle))


"""########### Challenge 5 - Draw a Random Walk and Color ########"""

"""My Solution"""
# import turtle 
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b


# direction = [0, 90, 180, 270]
# the_turtle.pensize(15)
# the_turtle.speed("fastest")

# for _ in range(200):
#     r, g, b = random_color()
#     the_turtle.pencolor((r,g,b))  
#     the_turtle.forward(30)
#     the_turtle.setheading(random.choice(direction))

"Angela Yu Solution"
import turtle 
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


direction = [0, 90, 180, 270]
the_turtle.pensize(15)
the_turtle.speed("fastest")

for _ in range(200):
    the_turtle.pencolor(random_color())  
    the_turtle.forward(30)
    the_turtle.setheading(random.choice(direction))






screen = Screen()
screen.exitonclick()