from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# 1. explicit wait is not global, it is only for certain element
# 2. implicit wait is global, for each element, poll DOM periodically until timeout


driver = webdriver.Chrome()
url = "http://the-internet.herokuapp.com/iframe"
driver.get(url)
driver.implicitly_wait(2)

# default content
print(driver.find_element_by_tag_name("h3").text)
# frame id, frame name
# <iframe id="mce_0_ifr" src="javascript:&quot;&quot;" frameborder="0" allowtransparency="true" title="Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help" style="width: 100%; height: 100px; display: block;">
# </iframe>
driver.switch_to.frame("mce_0_ifr") # use id="mce_0_ifr"
# text_field = driver.find_element_by_xpath("//[text()='Your content goes here.']")
text_field = driver.find_element_by_css_selector("body#tinymce")
# text_field.click()
time.sleep(2)
text_field.clear()
time.sleep(2)
text_field.send_keys("Test in in process!!!")
# print(driver.find_element_by_tag_name("h3").text)
time.sleep(2)
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

time.sleep(3)
driver.close()