from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
url = "http://the-internet.herokuapp.com/windows"
driver.get(url)
driver.implicitly_wait(2)

click_here = driver.find_element(By.LINK_TEXT, "Click Here").click()
click_again = driver.find_element(By.LINK_TEXT, "Click Here").click()

driver.switch_to.window(driver.window_handles[2])
new_window = driver.find_element_by_tag_name("h3")
driver.close()

#
#

child_win  = driver.window_handles[1]

driver.switch_to.window(child_win)
# new_window = driver.find_element_by_tag_name("h3")
new_window =  driver.find_element(By.XPATH, "//h3[text()='New Window']")
print(f"new window is {new_window.text}")
time.sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.default_content()
time.sleep(3)
driver.close()

# driver.switch_to.window(driver.window_handles[0])
# new_window = driver.find_element_by_tag_name("h3")
# driver.close()
