from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
# ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://fortinet.com"
driver.get(url)
driver.implicitly_wait(2)

action = ActionChains(driver)

# right-click with context-click

# right-click, then inspect
# <input type="button" id="double-click" value="Double Click Me">
double_click_field = driver.find_element_by_id("double-click")
# right-click with context-click
action.context_click(double_click_field).perform()

# double-click
action.double_click(double_click_field).perform()

action.click(double_click_field)
action.click_and_hold(double_click_field)
action.context_click(double_click_field)
action.double_click(double_click_field)
action.drag_and_drop(double_click_field)
action.key_down()
action.move_to_element()
time.sleep(2)




# time.sleep(3)
driver.close()