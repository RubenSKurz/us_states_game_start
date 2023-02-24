import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
count = 0
guessed_correct = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 Guess the State", prompt="What is another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in data["state"].unique():
        if answer_state in guessed_correct:
            pass
        else:
            guessed_correct.append(answer_state)
            count += 1
            correct_state = turtle.Turtle()
            correct_state.penup()
            correct_state.hideturtle()
            state_data = data[data.state == answer_state]
            new_x = int(state_data["x"])
            new_y = int(state_data["y"])
            correct_state.goto(x=new_x, y=new_y)
            correct_state.write(answer_state, align="center", font=("Courier", 10, "normal"))
    if count == 50:
        game_is_on = False
    else:
        pass

all_states = [name for name in data["state"]]
states_to_learn = [name for name in all_states if name not in guessed_correct]

panda = pandas.DataFrame(states_to_learn)
panda.to_csv('list_to_learn.csv', index_label="column")
