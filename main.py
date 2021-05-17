# import statements
import turtle
import pandas

# printing the map to the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading csv using pandas library and storing it in data variable
data = pandas.read_csv("50_states.csv")

# changing data to list
states = data.state.to_list()

# initializing array called guessed that will store the guessed state as
guessed = []

# prompting the user for an answer and storing it
while len(guessed) < 50:
    # title case utilized in order to cap the first letter and lowercase the rest
    answer = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="Guess a State or type 'Exit' to quit").title()


    # including an EXIT so the user can quit the game
    if answer == "Exit":
        missed_states = [state for state in states if state not in guessed]
        # creating a data frame that holds the missed states
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States_To_Learn.csv")
        break

    # checking if the answers is in the states
    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guessed.append(answer)

        # creating a new variable called state data in which will hold the state data of the state
        # that the user provided
        state_choice = data[data.state == answer]

        # go to the position of the state
        t.goto(int(state_choice.x), int(state_choice.y))

        # writing the name of the state
        # item looks into the data and just grabs the first element
        t.write(state_choice.state.item())
