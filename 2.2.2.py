import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
res = calc(x)
pole = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", pole)
pole.send_keys(res)

sub = browser.find_element(By.XPATH, "//button[@type='submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);",sub)

one = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
one.click()

two = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
two.click()

sub.click()

time.sleep(5)