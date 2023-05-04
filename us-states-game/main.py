import turtle
import pandas

data = pandas.read_csv(
    "/Users/quoczuong/Udemy/Python/Code/FinalProject/us-states-game/50_states.csv")
list_of_state = data["state"]
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/quoczuong/Udemy/Python/Code/FinalProject/us-states-game/blank_states_img.gif"
screen.setup(height=491, width=725)


# dung de load file anh vao screen
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(
            "/Users/quoczuong/Udemy/Python/Code/FinalProject/us-states-game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
