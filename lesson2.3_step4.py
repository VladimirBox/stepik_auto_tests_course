from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Взаимодействие с модалкой
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    # ищем элемент (х) и записываев переменную
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text    

    # считаем значение и записываем в переменную(у)
    def calc(x):
       return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    # выводим переменную(у) в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    # Выводим ответ в консоль
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
