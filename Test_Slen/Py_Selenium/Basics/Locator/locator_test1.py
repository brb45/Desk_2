
# elem = driver.find_element_by_id()
# driver.find_element_by_class_name
# driver.find_element_by_name
# driver.find_element_by_xpath
# driver.find_element_by_css_selector
# driver.find_element_by_link_text
# driver.find_element_by_partial_link_text

#1. basic setup of chrome webdriver
from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
opt.add_argument('ignore-certificate-errors')
opt.add_argument('--allow-insecure-locolhost')

driver = webdriver.Chrome(options=opt)
url = 'https://yahoo.com'
# driver.get(url)
# driver.get(url)
# driver.get(url)
# time.sleep(5)
# driver.close()

#2.
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

print(driver.title)
print(driver.current_url)
# assert "ProtoCommerce" == driver.title
# assert url == driver.current_url