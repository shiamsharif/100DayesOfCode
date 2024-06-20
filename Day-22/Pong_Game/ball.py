from turtle import Turtle

class Ball(Turtle):
    
    def __init__(Self):
        super().__init__()
        Self.color("orange")
        Self.shape("circle")
        Self.penup()
        Self.x_move = 10
        Self.y_move = 10
        Self.move_Speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_Speed *= 0.9

    def reset(Self):
        Self.goto(0, 0)
        Self.move_Speed = 0.1
        Self.bounce_x()  