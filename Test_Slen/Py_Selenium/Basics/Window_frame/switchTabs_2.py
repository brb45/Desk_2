from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()

# <a id="opentab" class="btn-style class1 class2" href="https://www.rahulshettyacademy.com/" target="_blank">Open Tab</a>
# <button id="openwindow" class="btn-style class1" onclick="openWindow()">Open Window</button>
tab = 'openwindow'
tab = driver.find_element(By.ID, tab)
tab.click()

new_tab = driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
driver.close()
# http://www.qaclickacademy.com/


driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
# https://rahulshettyacademy.com/AutomationPractice/


























































































