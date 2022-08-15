from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    # Нажимаем кнопку во вкладке
    button = browser.find_element(By.ID, "book")
    button.click()

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
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    # Выводим ответ в консоль
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
