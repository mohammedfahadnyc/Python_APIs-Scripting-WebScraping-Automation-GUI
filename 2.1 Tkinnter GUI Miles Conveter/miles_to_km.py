from tkinter import *

window = Tk()
window.title("Miles to km Converter")
window.minsize(height=100,width=200)
window.config(padx=20,pady=20)

def action():
    miles = float(text_area.get())
    miles_to_km = miles*1.609
    ans_label.config(text=miles_to_km)

is_eql_label = Label(text="is equal to")
is_eql_label.grid(column=1,row=4)

text_area = Entry()
text_area.focus()
text_area.grid(row=3,column=2)


ans_label = Label(text="0")
ans_label.grid(row=4,column=2)

button = Button(text="Convert",command=action)
button.grid(row=5,column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=3,column=3)

km_label = Label(text="Km")
km_label.grid(row=4,column=3)



window.mainloop()