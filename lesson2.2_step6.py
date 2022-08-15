from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем элемент (х) и записываев переменную
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # считаем значение и записываем в переменную(у)
    
    def calc(x):
       return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # скролим до элементов
    browser.execute_script("window.scrollBy(0, 100);")

    # выводим переменную(у) в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # ищем и отмечаем checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    # ищем и выбираем radiobutton "Robots rule!"
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # ждем загрузки страницы
    time.sleep(1)

    # отправляем нажатием на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
