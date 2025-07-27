import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

fname = browser.find_element(By.XPATH, "//input[@name='firstname']")
lname = browser.find_element(By.XPATH, "//input[@name='lastname']")
email = browser.find_element(By.XPATH, "//input[@name='email']")
button = browser.find_element(By.XPATH, "//input[@id='file']")
submit = browser.find_element(By.XPATH, "//button[@type='submit']")

fname.send_keys('ueu')
lname.send_keys('2we')
email.send_keys('ee@ee.we')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
button.send_keys(file_path)
submit.click()

time.sleep(5)