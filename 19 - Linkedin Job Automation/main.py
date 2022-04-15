from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "pysmpt15@gmail.com"
ACCOUNT_PASSWORD = "123456Ab"
chrome_driver_path = "/Users/fahadsmacbook/Downloads/Python 100 Days/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()


email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)




jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in jobs :
    job.click()
    try :
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        mbl = driver.find_element_by_css_selector(".fb-single-line-text__input")
        mbl.send_keys("9293038523")
        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector(".artdeco-modal__confirm-dialog-btn .artdeco-button")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except :
        print("No apply button found")

