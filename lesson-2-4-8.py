
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# объявлем функцию calc(x) и задаем формулу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # ждем в течении 15 секунд, когда счет=100$ 
    element = WebDriverWait(browser, 15).until( 
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        
    # теперь нажимаем кнопку Book
    button = browser.find_element(By.ID, "book") 
    button.click()
   

    
    # считываем значение для переменной х
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    print (x)
    
    
    # выяисляем результат    
    y = calc(x)
    
        
    # ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # находим и нажимаем кнопку Submit
    button = browser.find_element(By.ID, "solve")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()