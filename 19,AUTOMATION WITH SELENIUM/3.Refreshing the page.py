from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.google.com')
driver.maximize_window()

time.sleep(3)

driver.refresh()

