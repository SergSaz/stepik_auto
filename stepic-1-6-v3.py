from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Автоматическая установка и настройка ChromeDriver
browser = webdriver.Chrome(ChromeDriverManager().install())

# Ваш код
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
browser.quit()