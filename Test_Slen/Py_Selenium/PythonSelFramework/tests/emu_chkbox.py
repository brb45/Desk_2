from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. Handle checkbox selections
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
checkboxes =  driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# <input id="checkBoxOption1" value="option1" name="checkBoxOption1" type="checkbox">

for checkbox in checkboxes:
    attribute_val = checkbox.get_attribute("value")
    print(attribute_val)
    if attribute_val == "option1":
        checkbox.click()
    assert checkbox.is_selected()

    time.sleep(1)
    break
driver.close()