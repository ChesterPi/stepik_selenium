from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    chislo1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    x = chislo1.text
    chislo2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    y = chislo2.text
    z = int(x) + int(y)
    browser.find_element(By.CSS_SELECTOR, "[id='dropdown']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, f"//option[@value='{z}']").click()
    button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    button.click()

finally:
     time.sleep(10)
 
     
     browser.quit()