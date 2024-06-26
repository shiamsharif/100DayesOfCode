import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "./blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title="Guess the State", prompt="what's another state's name?")

print(answer_state)





screen.exitonclick()