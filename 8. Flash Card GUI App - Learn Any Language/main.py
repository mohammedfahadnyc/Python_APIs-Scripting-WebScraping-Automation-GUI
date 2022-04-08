import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
from tkinter import messagebox
window = Tk()

window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("FlashCard Learn Language")

to_learn = []
word_pair = {}



try :
    data = pandas.read_csv("./data/to_learn_words.csv")
    to_learn = data.to_dict(orient="records")
except :
    data = pandas.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")


def add_to_known_list():
    global word_pair
    to_learn.remove(word_pair)
    learn_list = pandas.DataFrame(to_learn)
    learn_list.to_csv("./data/to_learn_words.csv",index=False)


def word_generator (bool) :
    if bool :
        messagebox.showinfo(title="Congrats", message="We will not show this word anymore")
    elif not bool  :
        messagebox.showinfo(title="Dont worry", message="We will again show this word ")
    if len(to_learn) == 0 :
        all_learnt()
    else:
        global flip_timer,word_pair
        word_pair = random.choice(to_learn)
        canvas.itemconfig(canvas_image, image=card_front_image)
        canvas.itemconfig(language_text, text="French")
        canvas.itemconfig(word_text, text=word_pair["French"])


def translator():
    global word_pair
    canvas.itemconfig(canvas_image,image=card_back_image)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=word_pair["English"])


def all_learnt():
    global flip_timer
    window.after_cancel(flip_timer)
    messagebox.showinfo(title="No Word Left", message="You've Learnt All Words")
    canvas.itemconfig(word_text, text="Congratulations! You've Learnt All Words", font=("Aerial", 20, "bold"))

def right_click():
    global flip_timer
    window.after_cancel(flip_timer)
    word_generator(True)
    flip_timer = window.after(3000,translator)
    add_to_known_list()


def wrong_click():
    global flip_timer
    window.after_cancel(flip_timer)
    word_generator(False)
    flip_timer = window.after(3000,translator)



def starter():
    global flip_timer, word_pair
    word_pair = random.choice(to_learn)
    flip_timer = window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=word_pair["French"])
    flip_timer = window.after(3000,translator)

flip_timer = window.after(3000,word_generator)


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front_image)
language_text =canvas.create_text(400,150,text="French",font=("aerial",40,"italic"))
word_text = canvas.create_text(400,263,text="Word",font=("aerial",60,"bold"))
canvas.config(highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)



right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image,highlightthickness=0,command=right_click)
right_button.grid(row=1,column=0)
wrong_button = Button(image=wrong_image,highlightthickness=0,command=wrong_click)
wrong_button.grid(row=1,column=1)
start_button = Button(text="Start",command=starter)
start_button.grid(row=2,column=0,columnspan=2)




window.mainloop()
