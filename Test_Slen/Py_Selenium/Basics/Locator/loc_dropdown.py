from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_argument("headless")

driver = webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
#@@ 1. static drop down
# tag: select
#  provide methods to  handle options in drop-down menu

from selenium.webdriver.support.select import Select
# <select class="form-control" id="exampleFormControlSelect1">
#         <option>Male</option>
#         <option>Female</option>
# </select>
drop_down= driver.find_element_by_css_selector("select#exampleFormControlSelect1")
print(drop_down)
# <selenium.webdriver.remote.webelement.WebElement
# (session="c16d0d074c7ff5b3622c7b902928144d",
# element="de98f9ef-73bb-4168-a0e1-171702e64ee4")>

dropdown = Select(drop_down)
print(dropdown)
# <selenium.webdriver.support.select.Select object at 0x03620CF0>

# 1.1 select_by_visible_text
text = "Female"
dropdown.select_by_visible_text(text)
# dropdown.select_by_value()
# dropdown.deselect_by_visible_text()
time.sleep(2)
text = "Male"
dropdown.select_by_visible_text(text)
driver.save_screenshot("dropdown.png")
time.sleep(2)

# 1.2 select_by_index
dropdown.select_by_index(1)
time.sleep(10)
dropdown.select_by_index(0)

# 1.3 select_by_value

# @@ 2. Dynamic DropDown





time.sleep(2)
driver.close()


























































































