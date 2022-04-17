import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

google_forms = "https://forms.gle/WEqXfQVAaETuXSRd8"
chrome_driver_path = "/Users/fahadsmacbook/Downloads/Python 100 Days/Development/chromedriver"


headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.9'
}
zillow = "https://www.zillow.com/manhattan-new-york-ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Manhattan%2C%20New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.21193864990235%2C%22east%22%3A-73.74570635009766%2C%22south%22%3A40.64962598893827%2C%22north%22%3A40.91167454937798%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12530%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
data = requests.get(url=zillow,headers=headers).text

soup = BeautifulSoup(data,"html.parser")

names_list = soup.find_all(name="address",class_="list-card-addr")
names_list = [name.text for name in names_list]
# print(names_list)

price_list = soup.find_all(name="div",class_="list-card-price")
price_list = [price.text for price in price_list]
# print(price_list)

links_list = soup.find_all(name="a",class_="list-card-link")
links_list = [link.get("href") for link in links_list]
new_links_list = []

# print(links_list)

for link in links_list :
    if "https://www.zillow.com" not in link :
        link = 'https://www.zillow.com/'+link
    new_links_list.append(link)

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


for i in range (len(names_list)) :
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    data = driver.get(google_forms)
    time.sleep(2)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(names_list[i])
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(price_list[i])
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(new_links_list[i])
    time.sleep(1)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    driver.quit()

