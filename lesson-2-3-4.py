
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# объявлем функцию calc(x) и задаем формулу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # находим и нажимаем первую кнопку 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    #подтверждаем "да" в модальном окне
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # считываем значение для переменной х
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    
    # выяисляем результат    
    y = calc(x)
    
        
    # ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)


    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()