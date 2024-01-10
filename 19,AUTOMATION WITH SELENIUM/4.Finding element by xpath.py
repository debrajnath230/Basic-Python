from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys('iphones')
driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()

time.sleep(5)

# Use find_elements to get a list of elements
product_list = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')

# Print the number of products found
print(str(len(product_list)) + ' products found')

# Print the text of each product
for product in product_list:
    print(product.text)

driver.quit()
