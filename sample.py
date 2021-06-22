import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

path = './library/chromedriver'
url='https://courses.letskodeit.com/login'
driver = Chrome(executable_path=path)
driver.get(url=url)
driver.maximize_window()
driver.find_element_by_id('email').send_keys('test@gmail.com')
driver.find_element_by_id('password').send_keys('123324')
driver.find_element_by_xpath('//input[@value="Login"]').click()
time.sleep(10)
#driver.find_element_by_xpath('//span[@class="caret"]').click()
#driver.find_element_by_link_text('Logout').click()
#wait = WebDriverWait(driver,20)
#element = wait.until(ec.visibility_of_element_located((By.XPATH,'//img[@class="z1-navbar-rhs-img')))
#element = driver.find_element_by_xpath('//img[@class="zl-navbar-rhs-img"]')
element = driver.find_element_by_xpath('//span[@class="dynamic-text help-block"]')
if element:
  print('yes found')
driver.quit()