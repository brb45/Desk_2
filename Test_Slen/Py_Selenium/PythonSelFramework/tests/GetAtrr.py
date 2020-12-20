from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.implicitly_wait(2)

# <input class="form-control ng-pristine ng-invalid ng-touched" minlength="2" name="name" required="" type="text">
name_field =  driver.find_element(By.NAME, "name")
name_field.clear()
name_field.send_keys("SSQA")
# print(name_field.text) # Not working, selenium can't print filled-out info through text
print(name_field.get_attribute("value")) # SSQA
print(name_field.get_attribute("name"))  # name
print(name_field.get_attribute("class"))  # form-control ng-untouched ng-dirty ng-valid

rst = driver.execute_script('return document.getElementsByName("name")[0].value')  # SSQA
print(rst)


time.sleep(3)
driver.close()