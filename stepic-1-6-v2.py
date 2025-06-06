import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

# Инициализируем переменную browser до блока try
browser = None

try:
    browser = webdriver.Chrome()  # Инициализация браузера
    browser.get(link)  # Переход по ссылке
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")  # Поиск кнопки
    time.sleep(5)
    button.click()  # Нажатие на кнопку

except Exception as e:
    # Логируем ошибку, если она возникла
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер, если он был инициализирован
    if browser:
        browser.quit()