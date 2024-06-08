# import colorgram 

# rgb_colors = []
# colors = colorgram.extract('./image.jpg',40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
the = turtle_module.Turtle()
the.speed("fastest")
the.penup()
the.hideturtle()


color_list = [(213, 10, 25), (107, 104, 62), (178, 166, 125), (247, 30, 78), (231, 215, 195), (40, 39, 22), (133, 148, 81), (67, 78, 34), (200, 202, 154), (248, 111, 151), (250, 153, 182), (245, 202, 218), (79, 92, 73), (27, 36, 23), (223, 23, 47), (35, 41, 45), (247, 10, 45), (191, 93, 79), (174, 20, 16), (73, 82, 88), (231, 173, 162), (141, 175, 122), (73, 8, 12), (113, 149, 87), (53, 78, 36), (237, 240, 238), (230, 233, 237), (155, 164, 172), (56, 66, 69), (57, 64, 71), (173, 203, 153), (113, 127, 145), (182, 195, 199), (242, 14, 14), (120, 130, 133), (179, 193, 206)]


the.setheading(225)
the.forward(300)
the.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    the.dot(20, random.choice(color_list))
    the.forward(50)

    if dot_count % 10 == 0:
        the.setheading(90)
        the.forward(50)
        the.setheading(180)
        the.forward(500)
        the.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()