from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
#driver2 = webdriver.Chrome()

# untuk memperbesar window
driver.maximize_window()


# driver1.get('https://idejongkok.com')
# sleep(2)

# driver2.get('https://google.com')
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)

# driver.get('https://www.saucedemo.com/')
# driver.find_element(By.ID,'user-name').send_keys('standard_user')
# driver.find_element(By.ID,'password').send_keys('secret_sauce')
# sleep(5)
# driver.find_element(By.ID,'login-button').click()