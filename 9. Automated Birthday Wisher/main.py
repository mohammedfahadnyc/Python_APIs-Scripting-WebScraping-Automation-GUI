import random

import pandas
import datetime
import smtplib

current_day = datetime.datetime.now()
month = current_day.month
day = current_day.day
today = (month,day)
sender = "pysmpt15@gmail.com"
sender_password = "123456Ab"
PLACEHOLDER = "[NAME]"


with open(file=f"./letter_templates/letter_{random.randint(1,3)}.txt") as letters:
    letter = letters.read()


data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month,row.day) : row for (index,row) in data.iterrows()}


def send_email(to_address,message) :
    with smtplib.SMTP("smtp.gmail.com",587) as connection :
        connection.starttls()
        connection.login(user=sender,password=sender_password)
        connection.sendmail(from_addr=sender,
                            to_addrs=to_address,
                            msg=f"Subject:Birthday Wish \n\n {message}")



def birthday_match():
    global letter
    if today in birthday_dict :
        person = birthday_dict[today]["name"]
        email = birthday_dict[today]["email"]
        letter = letter.replace("[NAME]",person)
        send_email(email,letter)


birthday_match()
print(letter)
