from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    time.sleep(2)

    check_box = browser.find_element(By.ID,'robotCheckbox')
    check_box.click()

    time.sleep(2)

    check_box = browser.find_element(By.ID, 'robotsRule')
    check_box.click()

    time.sleep(2)

    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()


    time.sleep(2)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()