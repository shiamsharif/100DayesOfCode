from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(Self):
        super().__init__()
        Self.color("white")
        Self.penup()
        Self.hideturtle()
        Self.l_score = 0
        Self.r_score = 0
        Self.update_scoreboard()
       
    
    def update_scoreboard(Self):
        Self.clear( )
        Self.goto(-100, 200)
        Self.write(Self.l_score, align="center", font=("Courier", 80, "normal"))
        Self.goto(100, 200)
        Self.write(Self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(Self):
        Self.l_score += 1
        Self.update_scoreboard()

    def r_point(Self):
        Self.r_score += 1
        Self.update_scoreboard()

    