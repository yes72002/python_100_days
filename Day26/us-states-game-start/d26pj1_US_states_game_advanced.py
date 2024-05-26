import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Games")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

writting = turtle.Turtle()
writting.penup()
writting.hideturtle()
guessed_states = []
# avoid double score
check_state = [0] * len(states_list)
# print(check_state)
# print(len(check_state))
# print(sum(check_state))

is_going_on = True
while is_going_on:
    answer_state = screen.textinput(
        title=f"{sum(check_state)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        is_going_on = False
        # break
    elif answer_state in states_list:
        check_state[states_list.index(answer_state)] = 1
        guessed_states.append(answer_state)
        correct_state = data[data["state"] == answer_state]
        x = int(correct_state.x)
        y = int(correct_state.y)
        # print(x)
        # print(y)
        writting.goto(x, y)
        writting.write(f"{answer_state}", True, align=ALIGNMENT, font=FONT)
    else:
        # move the cursor back to the textinput window.
        writting.write(f"", True, align=ALIGNMENT, font=FONT)
    # complete all states
    if sum(check_state) == 50:
        is_going_on = False

# states to learn.csv
missing_states = [state for state in states_list if state not in guessed_states]
# print(missing_states)

missing_states_dict = {"state": missing_states}
learn = pandas.DataFrame(missing_states_dict)
learn.to_csv("states_to_learn.csv")

