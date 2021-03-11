from selenium import webdriver
import time

# Regular checkbox
#
# checkbox.is_displayed()
# checkbox.is_enabled()
# checkbox.is_selected()
# checkbox.get_attribute('value')

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

time.sleep(2)
# @@ 3. checkbox
# <input id="checkBoxOption1" value="option1" name="checkBoxOption1" type="checkbox">
xpath_sel = "//input[@type='checkbox']" #//input[@type='checkbox']

# find_elements not find_element

checkboxes = driver.find_elements_by_xpath(xpath_sel)
# print(len(checkboxes)) # 3
# print(checkboxes[0].id)
# time.sleep(20)
for checkbox in checkboxes:
    if checkbox.get_attribute('value') =='option2':
        checkbox.click()
        assert checkbox.is_selected()
        print(f"id is {checkbox.get_attribute('id')}")
        print(f"value is {checkbox.get_attribute('value')}")
        print(f"name is {checkbox.get_attribute('name')}")
        print(f"type is {checkbox.get_attribute('type')}")

#
# id is checkBoxOption2
# value is option2
# name is checkBoxOption2
# type is checkbox
time.sleep(2)
driver.close()


























































































