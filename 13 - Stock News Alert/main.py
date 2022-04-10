import requests
import datetime
import os
from twilio.rest import Client

FLUCTUATION = 2.5

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

STOCK_PRICE_API_KEY = os.environ.get("STOCK_PRICE_API_KEY")

stock_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : STOCK_PRICE_API_KEY
}
"function=&symbol=TSLA&outputsize=compact&apikey=NBYFQW7YJ81S0KQD"

stock_get_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=compact&apikey=NBYFQW7YJ81S0KQD"


twillo_sid = os.environ.get("OWN_SID")
twillo_auth_token = os.environ.get("OWN_TWILLO_AUTH_TOKEN")
FROM_NUMBER = os.environ.get('OWN_TWILLO_FROM_NUMBER')
TO_NUMBER = os.environ.get('OWN_TWILLO_GET_NUMBER')

today = str(datetime.datetime.today())
today = today.split(" ")[0]

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "c933a0c2406d4437944f9838494f38d5"

news_get_url = "https://newsapi.org/v2/everything?q=Tesla&from=2022-04-10&sortBy=popularity&language=en&apiKey=c933a0c2406d4437944f9838494f38d5"
#
# news_api_parameter = {
#     "q" : COMPANY_NAME,
#     "from" : today,
#     "sortBy" : "popularity",
#     "language" : "en",
#     "apiKey" : NEWS_API_KEY
# }
news_api_parameter = {
    "qInTitle" : COMPANY_NAME,
    "apiKey" : NEWS_API_KEY
}

tesla_closing_price_today = 1
tesla_closing_price_yesterday = 1



def generate_articles():
    response = requests.get(url=NEWS_ENDPOINT,params=news_api_parameter)
    response = response.json()
    articles_list = response["articles"]
    if len(articles_list) > 3 :
        articles_list = [articles_list[i] for i in range(3)]
    else :
        articles_list = [articles_list[i] for i in range(len(articles_list))]
    return articles_list


def send_messge(difference_percentage,difference_percentage_abs):
    articles_list = generate_articles()
    account_sid = twillo_sid
    auth_token = twillo_auth_token

    client = Client(account_sid, auth_token)

    if difference_percentage > 0:
        symbol = "🔺"
    elif difference_percentage < 0:
        symbol = "🔻"
    for i in range(len(articles_list)):
        title = articles_list[i]["title"]
        description = articles_list[i]["description"]
        print(f"News {1} : {title},{description}")
        message = client.messages \
            .create(
            body=f"{STOCK} {symbol} {difference_percentage_abs} %,Headline:{title}, News : {description} ",
            from_=FROM_NUMBER,
            to= TO_NUMBER
        )
        print(message.status)


def get_alert():
    response = requests.get(url=STOCK_ENDPOINT,params=stock_parameter)
    response.raise_for_status()
    data = response.json()
    data_list = data["Time Series (Daily)"]
    new_data_list_price = [value for (key,value) in data_list.items()]
    # print(new_data_list_price)
    tesla_closing_price_yesterday = float(new_data_list_price[1]["4. close"])
    tesla_closing_price_today = float(new_data_list_price[0]["4. close"])
    difference = tesla_closing_price_today-tesla_closing_price_yesterday

    difference_percentage = (difference / abs(tesla_closing_price_yesterday))*100
    difference_percentage_abs = abs(difference_percentage)

    # print(tesla_closing_price_today,tesla_closing_price_yesterday)
    # print(difference_percentage)

    if difference_percentage_abs > FLUCTUATION+500 :
        send_messge(difference_percentage,difference_percentage_abs)
    else :
        print(f"Not Much Fluctuation In News Today for {COMPANY_NAME}")


get_alert()




