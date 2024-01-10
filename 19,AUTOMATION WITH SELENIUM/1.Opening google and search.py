from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')
driver.maximize_window()

input_field = driver.find_element(By.NAME, 'q')
input_field.send_keys('python')
time.sleep(0.5)

# Find the search button by XPath using By.XPATH
button = driver.find_element(By.XPATH, "//input[@value='Google Search']")
button.click()
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.quit()
