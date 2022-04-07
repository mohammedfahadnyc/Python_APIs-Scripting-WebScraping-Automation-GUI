import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


window = Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=100,bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(height=220, width=230)
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.create_image(115,109,image=tomato_image)
canvas_text = canvas.create_text(115,120,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=2,column=2)


def count_down(count) :
        minute = math.floor(count/60)
        second = count % 60
        if second < 10 :
            second = f"0{second}"
        canvas.itemconfig(canvas_text, text=f" {minute} : {second}")
        if count >= 0:
            global timer
            timer = window.after(1000, count_down, count - 1)
        else :
            start_action()
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range (work_sessions) :
                marks += "✓"
            checkbox_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

def start_action():
    global reps
    reps += 1
    if reps % 8 == 0 :
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0 :
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break!", fg=PINK)
    else :
        count_down(WORK_MIN)
        timer_label.config(text="Work!", fg=GREEN)



#calls action() when pressed
button_start = Button(text="Start", command=start_action,highlightthickness=0)
button_start.config(fg=GREEN)
button_start.grid(row=3,column=1)

timer_label = Label(text="Timer")
timer_label.config(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
timer_label.grid(row=1,column=2)

def reset_action():
    # canvas.itemconfig(canvas_text,text="00:00")
    global timer,reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(canvas_text,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
    timer_label.config(text="Timer",font=(FONT_NAME,20,"normal"))
    checkbox_label.config(text="")


#calls action() when pressed
button_reset = Button(text="Reset", command=reset_action,highlightthickness=0)
button_reset.config(fg=RED)
button_reset.grid(row=3,column=3)


checkbox_label = Label(text="",bg=YELLOW,fg=GREEN)
checkbox_label.grid(row=4,column=2)
window.mainloop()
