
CHROME_DRIVER_PATH = chrome_driver_path = "/Users/fahadsmacbook/Downloads/Python 100 Days/Development/chromedriver"


from Bot import InternetSpeedTwitterBot


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()
