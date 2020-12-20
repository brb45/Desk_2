from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
# checkbox.is_displayed()
# checkbox.is_enabled()
# checkbox.is_selected()
# checkbox.get_attribute('value')

# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()
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
        print(True)






time.sleep(2)



time.sleep(2)
driver.close()


























































































