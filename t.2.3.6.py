from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
import os
def calc(y):
    return str(math.log(abs(12 * math.sin(int(y)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text

    d = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(d)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()