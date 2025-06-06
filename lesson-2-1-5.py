
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# объявлем функцию calc(x) и задаем формулу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # берем число из картинки "сундука"
    sunduk = browser.find_element(By.ID, "treasure")  #находим конкретный тег по ID
    x = sunduk.get_attribute("valuex")  # смотрим у него атрибут checked (есть/нет)
    #print("Значение радиобатона peopleRule: ", people_checked
    print("Значение под сундуком: ", x)

    
    # считываем значение для переменной х
    #x_element = browser.find_element(By.ID, "input_value")
    #x = x_element.text
    
    
    # выяисляем результат    
    y = calc(x)
    
        
    # ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
   

    # выбираю чек-бокс I'm the robot
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()


    # выбираю радио-батон "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()


    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()