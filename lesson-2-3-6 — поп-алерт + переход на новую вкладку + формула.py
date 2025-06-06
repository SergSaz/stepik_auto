
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# объявлем функцию calc(x) и задаем формулу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # находим и нажимаем первую кнопку 
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    
    #переходим на другую вкладку
    new_window = browser.window_handles[1] # делаем запрос на вкладки и присваиваем второй вкладе имя new_window
    browser.switch_to.window(new_window)  # переход на вкладку с именем new_window
    
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