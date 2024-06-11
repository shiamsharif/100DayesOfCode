from turtle import Turtle, Screen

""" Create Game Display OR Screen """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
 
""" Create a Sncke Body """ 
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    # new_segment.color("white")
    if position[0] == 0 and position[1] == 0:
        new_segment.color("red")
    else:
        new_segment.color("white")
    new_segment.goto(position)
    









screen.exitonclick()