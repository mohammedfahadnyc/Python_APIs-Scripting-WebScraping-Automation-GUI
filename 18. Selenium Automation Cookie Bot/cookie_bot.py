

from selenium import webdriver
import time



path = "/Users/fahadsmacbook/Downloads/Python 100 Days/Development/chromedriver"

driver = webdriver.Chrome(executable_path=path)


#Selenium Auto Form Filler
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id('bigCookie')
driver.maximize_window()
def upgrade_cookie(cookie_count):
    price = driver.find_elements_by_css_selector("#products   .price")
    id = driver.find_elements_by_css_selector("#products   .price")
    id_list = [id.get_attribute('id') for id in id]
    print(id_list)
    price = [price.text for price in price]
    print(price)
    for i in range(len(price)):
        if price[i] == "":
            price = price[:i]
            break

    # price = [int(price) for price in price]
    new_price = []
    for a in price:
        b = ""
        a = a.split(",")
        for a in a:
            b = b + a
        b = int(b)
        new_price.append(b)
    print(new_price)
    dict = {new_price[i]: id_list[i] for i in range(len(new_price))}
    print(dict)

    cookie_count = driver.find_element_by_id("cookies")
    cookie_count = int(cookie_count.text.split(" ")[0])
    print(cookie_count)
    cookie_count = cookie_count
    upgrade_price = [money for money in new_price if money < cookie_count]
    print(upgrade_price)
    buy_price = max(upgrade_price)
    to_purchase_id = dict[buy_price]
    print(to_purchase_id)
    buy = driver.find_element_by_id(to_purchase_id)

    # buy.click()



delay=60*15    ###for 15 minutes delay
close_time=time.time()+delay
timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()
    if time.time() > timeout:
        upgrade_cookie()

    timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break





