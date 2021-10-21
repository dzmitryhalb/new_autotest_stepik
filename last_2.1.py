from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    s = browser.find_element_by_id("treasure")
    s1 = s.get_attribute("valuex")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    d = calc(s1)

    l = browser.find_element_by_id('answer')
    l.send_keys(d)

    check_box = browser.find_element(By.ID,'robotCheckbox')
    check_box.click()

    check_box = browser.find_element(By.ID, 'robotsRule')
    check_box.click()

    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

