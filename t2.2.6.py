from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def fun(y):
    return str(math.log(abs(12 * math.sin(int(y)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("input_value").text




    d = fun(a)

    #button = browser.find_element(By.CLASS_NAME, 'btn')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)



    #browser.execute_script("window.scrollBy(0, 120);")

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(d)

    button1 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)

    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()





    check_box = browser.find_element(By.ID, 'robotsRule')
    check_box.click()



    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(d)