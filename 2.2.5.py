from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"
browser.get(link)

sub1 = browser.find_element(By.XPATH, "//button[@type='submit']")
sub1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(y):
    return str(math.log(abs(12 * math.sin(y))))

x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
pol = browser.find_element(By.XPATH, "//input[@id='answer']")
sub = browser.find_element(By.XPATH, "//button[@type='submit']")

a = float(x)


pol.send_keys(calc(a))
sub.click()
time.sleep(10)