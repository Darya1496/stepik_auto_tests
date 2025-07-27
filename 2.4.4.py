from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element(By.ID, "book")
button.click()


def calc(y):
    return str(math.log(abs(12 * math.sin(y))))

x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
pol = browser.find_element(By.XPATH, "//input[@id='answer']")
sub = browser.find_element(By.XPATH, "//button[@type='submit']")

a = float(x)


pol.send_keys(calc(a))
sub.click()
time.sleep(10)