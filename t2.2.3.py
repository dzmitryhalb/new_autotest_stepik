from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1").text
    #a1 = a.get_attribute("num1")

    b = browser.find_element_by_id("num2").text
    #b1 = b.get_attribute("num1")

    c = str(int(a) + int(b))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(c)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(c)