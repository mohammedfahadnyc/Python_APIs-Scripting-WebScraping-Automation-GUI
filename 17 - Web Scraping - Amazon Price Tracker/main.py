import requests
import os
from bs4 import BeautifulSoup
import lxml
import smtplib



amazon_product_link = "https://www.amazon.com/Alpine-Corporation-Mirror-Waterfall-Fountain/dp/B002NU32N2/ref=sr_1_5?keywords=home+fountain+indoor&qid=1649915512&sprefix=home+foun%2Caps%2C77&sr=8-5"
PRICE = 0
FROM_EMAIL = os.environ.get("FROM_EMAL")
TO_EMAIL =  os.environ.get("TO_EMAL")
FROM_PASSWORD =  os.environ.get("FROM_PASSWORD")
DESIRED_PRICE = 500.00


def send_email() :
    global PRICE
    with smtplib.SMTP("smtp.gmail.com",587) as connection :
        connection.starttls()
        connection.login(user=FROM_EMAIL,password=FROM_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,to_addrs=TO_EMAIL,msg=f"Subject: Amazon Price Drop Alert \n\n Price For your product is now dropped to ${PRICE}. Buy it here {amazon_product_link}. ")
        print("Success")



def get_price():
    global PRICE
    headers = {
        "Accept-Language" : os.environ.get("ACCEPT_LANGUAGE"),
        "User-Agent":os.environ.get("USER_AGENT")
    }

    soup = BeautifulSoup(requests.get(url=amazon_product_link,headers=headers).text,"lxml")
    PRICE = float(soup.find(name="span",class_="a-price-whole").text)


get_price()
if PRICE < DESIRED_PRICE :
    send_email()

