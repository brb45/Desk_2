from selenium import webdriver

import time
# Chrome Option

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
print(driver.title)  # ProtoCommerce












time.sleep(3)
driver.close()