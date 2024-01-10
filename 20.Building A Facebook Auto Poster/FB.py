from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


driver= webdriver.Chrome()
driver.get('http://www.facebook.com')

emailelement = driver.find_element(By.XPATH,'.//*[@id="email"]')
emailelement.send_keys('debrajnath230@gmail.com')
passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
passelement.send_keys('Raj@9706934428')

login_button = driver.find_element(By.NAME, 'login')
login_button.click()

statuselement = driver.find_element(By.XPATH, "//div[@role=\"button\" and @class=\"x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou\"]")
time.sleep(2)
statuselement.click()
statuselement.send_keys('Hi There')
time.sleep(5)
buttons = driver.find_elements(By.TAG_NAME,'button')
time.sleep(5)

for button in buttons:
    if button.text =='Post':
        button.click()
        
driver.quit()