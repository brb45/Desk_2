from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

# https://rahulshettyacademy.com/seleniumPractise/#/
# //div[@class='product-action']/button/parent::div/parent::div
#
#explicit wait:
#
# Not global, only apply for target execution

# alert = driver.switch_to.alert
# alert.accept()
# Java, javascript alert
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
# url = "https://rahulshettyacademy.com/AutomationPractice/"

# driver.implicitly_wait(1000)
# url ="https://rahulshettyacademy.com/seleniumPractise/"

url = "https://the-internet.herokuapp.com/windows"
driver.get(url)
# driver.maximize_window()
# <a href="/windows/new" ,="" target="_blank">Click Here</a>
link_text = 'Click Here'
driver.find_element_by_link_text(link_text).click()

childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)

print(driver.find_element_by_tag_name("h3").text)
assert driver.find_element_by_tag_name("h3").text == "New Window"
driver.close()

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
# print(driver.find_element_by_tag_name("h3").get_attribute('value'))
assert driver.find_element_by_tag_name("h3").text == "Opening a new window"


time.sleep(3)
driver.close()


























































































