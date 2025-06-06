
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

    
try: 
    link = "https://suninjuly.github.io/selects1.html"
    #link = "https://suninjuly.github.io/selects2.html"  #проверочное задание из этого же задания
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "num1").text  # <- добавьте .text
    int_num1 = int(num1)
    print ("первое число: ", int_num1)
    
    
    num2 = browser.find_element(By.ID, "num2").text  # <- добавьте .text
    int_num2 = int(num2)
    print ("второе число: ", int_num2)
    
    # вычисляем результат    
    y = int_num1 + int_num2
    print (y)
    
    # импортируем библиотеку дропдауна
    from selenium.webdriver.support.ui import Select
    
    dropdown = Select(browser.find_element(By.ID, "dropdown")) # находим дропдаун - можно не кликать на него, так как импортировали библиотеку дропдаун
    dropdown.select_by_value(str(y))  # Выбираем вариант, где value="y"
    

    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
  