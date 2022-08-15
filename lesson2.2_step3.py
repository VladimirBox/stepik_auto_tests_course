from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем элемент (х) и записываев переменную
    x_element = browser.find_element(By.ID, "num1")
    x = int (x_element.text)

    # ищем элемент (y) и записываев переменную
    y_element = browser.find_element(By.ID, "num2")
    y = int (y_element.text)

    # считаем значение (z)
    z = str (x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(z)

    # ждем загрузки страницы
    time.sleep(1)

    # отправляем нажатием на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
