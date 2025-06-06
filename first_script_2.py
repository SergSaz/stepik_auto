from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_chrome_driver():
    # Create ChromeOptions instance
    options = Options()
    
    # Add various options to make the browser more stable
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-web-security')  # Disable web security
    options.add_argument('--allow-running-insecure-content')  # Allow running insecure content
    options.add_argument('--disable-webrtc')  # Disable WebRTC
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    #driver = webdriver.Chrome(options=options)  # or webdriver.Chrome(), etc.
    
    # Optional: Run in headless mode if you don't need to see the browser
    # options.add_argument('--headless')


#import time

# webdriver это и есть набор команд для управления браузером
#from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")


# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)


# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")


# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()





#ПОЛНЫЙ ответ: вам нужно отключить ведение журнала с помощью:-
#options = Options()
#options.add_argument('--headless')
#options.add_argument('log-level=3')
#driver = webdriver.Chrome(options=options)  # or webdriver.Chrome(), etc.

#but you cannot get rid of the console log output of:-
#DevTools прослушивает ws://127.0.0.1:#####/devtools/browser*****

#Вы просто прекратите запись сообщений Selenium в терминал/консоль.