from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. radiobutton selections
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
# <input value="radio1" name="radioButton" class="radioButton" type="radio">
radiobuttons =  driver.find_elements(By.NAME, "radioButton")

for radiobutton in radiobuttons:
    attribute_val = radiobutton.get_attribute("value")
    print(attribute_val)
    if attribute_val == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        time.sleep(1)
        break



driver.close()