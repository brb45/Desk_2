from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# opt = webdriver.ChromeOptions()
# opt.add_argument('ignore-certificate-errors')
# opt.add_argument('--allow-insecure-locolhost')
# driver = webdriver.Chrome(options=opt)


# webElement = driver.find_element_by_id(locator)
# webElement actions
# send_keys("content"), click(), text,clear()
# get_attribute('attribute')

# driver actions
# driver.title
# driver.maximize_window()
# driver.current_url
# driver.close()
# driver.quit()
# driver.

# elem = driver.find_element_by_id()
# driver.find_element_by_class_name
# driver.find_element_by_name
# driver.find_element_by_xpath
# driver.find_element_by_css_selector
# driver.find_element_by_link_text
# driver.find_element_by_partial_link_text

# driver.close() --> close current tab
# driver.quit()  --> close all tabs
# driver.refresh()
# driver.forward()
# driver.back()

#------------------------------------------------------

# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
url = "https://www.makemytrip.com/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
driver.close()

# @@ 2. Dynamic DropDown
# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted

# <input data-cy="fromCity" id="fromCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Delhi">
driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(5)

element = driver.find_element_by_id("fromCity")
# element = driver.find_element_by_xpath("//input[contains(@id, 'fromC')]")
# element = driver.find_element_by_xpath("//input[contains(@class, latoBlack)]")
time.sleep(2)
element.click()
#
# Interesting ###
css_sel = "input[placeholder='From']"
css_selector = driver.find_element_by_css_selector(css_sel)
city_list = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f"num of cities is {len(city_list)}")

css_selector.send_keys("bkk")
# selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
time.sleep(2)

for city in city_list:

    if city.text  == "Bangkok, Thailand":
        print(city.text) # Bangkok, Thailand
        city.click()
        time.sleep(2)
        break


destination = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
print(destination.text) # Mumbai, India
time.sleep(2)
destination.click()
time.sleep(5)

print(driver.session_id)
# fc2e1bb0b59213ef134f86e9fff3a635

driver.close()


####


# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted: Element <p class="font14 appendBottom5 blackText">...</p>
# is not clickable at point (251, 567).
# Other element would receive the click: <iframe title="notification-frame-17303c6cc"
# name="notification-frame-17303c6cc" id="webklipper-publisher-widget-container-notification-frame"
# frameborder="0" marginheight="0" marginwidth="0" style="display: block; z-index: 16776272;
# position: fixed; visibility: visible; height: 100%; width: 100%; top: 0px; left: 0px; right: auto;"
# data-notification-layout-id="~184fc0b7" data-notification-layout-name="modal"></iframe>
#   (Session info: chrome=86.0.4240.111)

























































































