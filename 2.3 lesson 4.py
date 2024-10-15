from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    otvet = browser.find_element(By.XPATH, "//input[@id='answer']")
    otvet.send_keys(y)
    button = browser.find_element(By.XPATH,"//button[@type='submit']")
    button.click()

finally:
   
    time.sleep(10)
 
    browser.quit()
