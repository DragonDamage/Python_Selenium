# pip install selenium
# python.exe -m pip install --upgrade pip
# Скачиваем нужный webdriver.Chrome с сайта https://googlechromelabs.github.io/chrome-for-testing/
import time
import os

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.google.ru/?hl=ru"
service = Service(executable_path="C:\\Users\\DragonDamage\\Desktop\\SeleniumProject\\chromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.maximize_window()
    driver.get(url=url)
    # driver.get(url="https://vk.com")
    time.sleep(5)

    search = driver.find_element(By.ID, 'APjFqb')  # Пишем куда нажать
    # search = driver.find_element(By.PARTIAL_LINK_TEXT, 'вводим текст со страницы').click  # Поиск по странице и клик на нужную кнопку
    # search = driver.find_element(By.CLASS_NAME, 'page_post_video'  # Поиск по классу
    search.clear()
    search.send_keys('тестовый поиск)')  # Вводимый текст
    search.send_keys(Keys.ENTER)         # Нажатие клавиши
    time.sleep(5)


    # driver.refresh()  # Обновить страницу
    # driver.get_screenshot_as_file("1.png")  # Сделать скрин
    # driver.save_screenshot("2.png")  # Сохранить скрин
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()  # Закрыть текущее окно
    driver.quit()   # Закрыть браузер





