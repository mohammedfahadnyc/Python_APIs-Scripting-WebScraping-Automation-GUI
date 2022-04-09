import time

THEME_COLOR = "#375362"

from quiz_brain import QuizBrain
from  tkinter import  *
from data import generate_question

class QuizInterFace :
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(fg="white",text=f"Score :0 ",bg=THEME_COLOR,highlightthickness=0)
        self.score_label.grid(row=0,column=1)
        self.question_canvas = Canvas(height=250,width=300,highlightthickness=0,bg="white")
        self.canvas_text = self.question_canvas.create_text(
            150,
            125,
            width = 280,
            text="Hello",
            font=("Arial",20,"italic"))
        self.question_canvas.grid(row=1,column=0,columnspan=2,pady=20)
        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_button_image,
            highlightthickness=0,
            command = self.true)
        self.true_button.grid(row=2,column=0)
        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_button_image,
            highlightthickness=0,
            command = self.false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")

        if  self.quiz_brain.still_has_questions() :
            self.score_label.config(text=f"Score :{self.quiz_brain.score} / {self.quiz_brain.question_number}")
            next_question = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.canvas_text, text=next_question)

        else :
            self.question_canvas.itemconfig(self.canvas_text, text="The End.Lets Begin New Game")
            # self.true_button.config(state="disabled")
            # self.false_button.config(state="disabled")
            self.quiz_brain.question_list = generate_question()
            self.quiz_brain.question_number = 0
            self.quiz_brain.score = 0
            self.window.after(2000,self.get_next_question)
            # self.get_next_question()


    def true(self):
        answer = self.quiz_brain.check_answer("True")
        self.feedback(answer)


    def false(self):
        answer = self.quiz_brain.check_answer("False")
        self.feedback(answer)


    def feedback(self,answer):
        if answer :
            self.question_canvas.config(bg="green")
        else :
            self.question_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)