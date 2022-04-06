import time
from turtle import Turtle,Screen
screen = Screen()
screen.setup(height=500,width=500)
screen.bgcolor("white")

turtle = Turtle()
turtle.hideturtle()
turtle.color("black")
turtle.penup()
screen.title("Welcome to WORD to NATO ALPHABET Phonetics Translator")
import pandas
data_frame = pandas.read_csv("/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Day 26 - List, Dict Comprehension, NATO/NATO-alphabet-start/nato_phonetic_alphabet.csv")


is_game_on = True
nato_dict = { row.letter : row.code for (index,row) in data_frame.iterrows() }
while is_game_on :
    time.sleep(0.5)
    word = screen.textinput("Please enter the word \n",prompt="enter").upper()
    word_to_letter_list = list(word)
    replacement_list =[ nato_dict[letter] for letter in word_to_letter_list]
    turtle.clear()
    turtle.goto(0,0)
    turtle.write(f"You've Entered {str(word)}" ,align="center",font=("aerial",18,"normal"))
    turtle.goto(0,-20)
    turtle.write(f"The NATO CODE is:",align="center",font=("aerial",18,"normal"))
    turtle.goto(0,-40)
    turtle.write(f"{replacement_list}",align="center",font=("aerial",12,"normal"))
    print(replacement_list)
    screen.update()

screen.exitonclick()