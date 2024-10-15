from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(y)
    сhckbx = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    сhckbx.click()
    radbtn = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radbtn.click()
    button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    button.click()

finally:
   
    time.sleep(10)
 
    browser.quit()

