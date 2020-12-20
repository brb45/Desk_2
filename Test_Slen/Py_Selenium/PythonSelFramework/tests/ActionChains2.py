from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
# ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://fortinet.com"
driver.get(url)
driver.implicitly_wait(2)

action = ActionChains(driver)
# <a class="nav-primary__listLink">Network Security</a>
# <a href="/products/next-generation-firewall.html">Next-Generation Firewalls</a>

element_1 = driver.find_element_by_xpath("//a[text()='Network Security']")
element_2 = driver.find_element_by_xpath("//a[text() = 'Next-Generation Firewalls']")
action.move_to_element(element_1).move_to_element(element_2).click().perform()
driver.save_screenshot("firewall.png")

time.sleep(3)
print(driver.title)
driver.close()