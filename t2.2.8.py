from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("Ivan")

    last = browser.find_element(By.NAME, "lastname")
    last.send_keys("Ivanov")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("gogle@mail.com")

    element = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    time.sleep(3)
    browser.quit()