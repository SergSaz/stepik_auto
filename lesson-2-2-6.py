
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# объявлем функцию calc(x) и задаем формулу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # считываем значение для переменной х
    x = browser.find_element(By.ID, "input_value").text
    print ("Число X: ", x)
    
    
    # вычисляем результат  
    y = calc(x)
    print ("Число Y: ", y)
        
    # ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
   

    # выбираю чек-бокс I'm the robot
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()


    # выбираю радио-батон "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2) #скролим вниз за футер
    option2.click()


    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  #скролим вниз за футер
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()