# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import pandas
FONT= ("Aerial",15,"normal")


window = Tk()
window.title("Welcome to Password Manager")
window.config(padx=50,pady=50)


def add_password():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    if len(password) <= 0 or len(email)  <= 0 :
        messagebox.showerror(title="Invalid Data",message="Please Enter Missing Data")
    else :
        save = messagebox.askokcancel(title="Confrim",message=f"Email is {email}, password is {password}")
        if save :
            with open(file="password.txt",mode="a") as file :
                file.write(f"\n {website}|  {email } |  {password} ")
                read_file = pandas.read_csv("password.txt")
                read_file.to_csv("password.csv")
            website_entry.delete(0,END)
            password_entry.delete(0,END)


def generate_password():
    password = password_generator.generate_random_password()
    password_entry.insert(0,password)
    pyperclip.copy(password)

image = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
logo = canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website :",font=FONT)
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username :",font=FONT)
email_label.grid(row=2,column=0)

password_label = Label(text="Password:",font=FONT)
password_label.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0,"exampleemail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
