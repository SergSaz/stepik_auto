
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


    
try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
        
    # ввести ответ в текстовое поле FirstNamme
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Sergey")
    
    # ввести ответ в текстовое поле LastNamme
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")
    
    # ввести ответ в текстовое поле Email
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("serg@mail.ru")
    
    #нажимаем кнопку Выберите файл и заказчиваем файл
    import os  #импортируем специальную библиотеку
    element = browser.find_element(By.ID, "file") #находим кнопку по ID
    current_dir = os.path.abspath(os.path.dirname(__file__)) #указываем что файл лежит в тойже директории, что и код
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла file.txt 
    element.send_keys(file_path) # загружаем файл



    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()