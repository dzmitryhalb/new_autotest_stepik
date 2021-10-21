from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(y):
    return str(math.log(abs(12 * math.sin(int(y)))))


    #butt = browser.find_element(By.ID, 'book')
    #butt.click()



    #button1 = browser.find_element(By.CLASS_NAME, "btn")
    #button1.click()

    #alert = browser.switch_to.alert
    #alert.accept()

    #x = browser.find_element_by_id("input_value").text

    #d = calc(x)

    #input = browser.find_element_by_id("answer")
    #input.send_keys(d)

    #button = browser.find_element(By.CLASS_NAME, "btn")
    #button.click()


try:
    #link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    #text_ = 100
    #locator = browser.find_element(By.ID, "price")
    #text_ = 100


    #element = browser.find_element(By.ID, 'price')

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button1 = browser.find_element(By.ID, 'book')
    button1.click()

    x = browser.find_element_by_id("input_value").text

    d = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(d)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(25)
    browser.quit()
