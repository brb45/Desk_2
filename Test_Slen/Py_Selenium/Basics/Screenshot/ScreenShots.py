from selenium import webdriver 
from time import sleep

browser = webdriver.Firefox() 
url = "https://www.lambdatest.com/"
browser.get(url)
sleep(1) 
browser.get_screenshot_as_file("get_screenshot_as_file.png")
browser.save_screenshot("save_screenshot.png")
browser.quit()

## Capturing Python Selenium Screenshots Of A Particular Element
