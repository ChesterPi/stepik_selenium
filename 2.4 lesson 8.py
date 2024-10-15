from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")
pravilo = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
button = browser.find_element(By.XPATH, "//button[@id='book']")
button.click()
x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = calc(x)
otvet = browser.find_element(By.XPATH, "//input[@id='answer']")
otvet.send_keys(y)
button = browser.find_element(By.XPATH,"//button[@type='submit']")
button.click()


time.sleep(10)
 
browser.quit()



