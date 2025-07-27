from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x_elem,y_elem):
    x = int(x_elem.text)
    y = int(y_elem.text)
    return str(abs(x + y))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num11 = browser.find_element(By.XPATH, "//span[@id = 'num1']")
    num22 = browser.find_element(By.XPATH, "//span[@id = 'num2']")

    res = calc(num11,num22)

    spisok = browser.find_element(By.XPATH, "//select[@id='dropdown']")
    spisok.click()
    w = browser.find_element(By.XPATH,f"//option[@value='{res}']")
    w.click()
    but = browser.find_element(By.XPATH, "//button[@type='submit']")
    but.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
