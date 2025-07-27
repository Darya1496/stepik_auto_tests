from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)

bob = browser.find_element(By.XPATH, "//button[@type='submit']")
bob.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(y):
    return str(math.log(abs(12 * math.sin(y))))

x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
pol = browser.find_element(By.XPATH, "//input[@id='answer']")
sub = browser.find_element(By.XPATH, "//button[@type='submit']")

a = float(x)


pol.send_keys(calc(a))
sub.click()
time.sleep(10)
