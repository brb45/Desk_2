from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
url = "https://www.makemytrip.com/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
# @@ 2. Dynamic DropDown
# <input data-cy="fromCity" id="fromCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Delhi">
element = driver.find_element_by_id("fromCity")
# element = driver.find_element_by_xpath("//input[contains(@id, 'fromC')]")
# element = driver.find_element_by_xpath("//input[contains(@class, latoBlack)]")
time.sleep(2)
element.click()
# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted

#

#
css_sel = "input[placeholder='From']"
css_selector = driver.find_element_by_css_selector(css_sel)
city_list = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f"num of cities is {len(city_list)}")

css_selector.send_keys("del")
time.sleep(2)

city_list = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f"num of cities is {len(city_list)}")
for c in city_list:
    if c.text  == "Delhi, India":
        # print(c.text)  Delhi, India
        c.click()
        time.sleep(2)
        break

destination = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
time.sleep(2)
destination.click()
time.sleep(2)

driver.close()


####
# <input data-cy="fromCity" id="fromCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Delhi">
element = driver.find_element_by_xpath("//input[contains(@class, latoBlack)]")
time.sleep(2)

element.send_keys("del")
time.sleep(2)

# <p class="font14 appendBottom5 blackText">Greenville, United States</p>
city_list = driver.find_elements_by_css_selector("p[class='font14 appendBottom5 blackText']")
print(f"num of cities is {len(city_list)}")
print(type(city_list))
# num of cities is 15
# <class 'list'>
# for city in city_list:
#     print(city)
    # < selenium.webdriver.remote.webelement.WebElement(session="f1436cb4c7e567aa5ae03ab932ebfae1",
    # element="b1c25272-089d-4a5f-89cc-74269449d375") >

for city in city_list:
    print(city.text)
    if city.text == "Capitan Corbeta CA Curbelo International Airport, Uruguay":
        print(f"found! {city.text}")
        city.click()
        break
        # time.sleep(3)
        # city.click()
        # time.sleep(3)
# selenium.common.exceptions.StaleElementReferenceException:
# Message: stale element reference: element is not attached to the page document
# time.sleep(30)
# city.click()

# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted: Element <p class="font14 appendBottom5 blackText">...</p>
# is not clickable at point (251, 567).
# Other element would receive the click: <iframe title="notification-frame-17303c6cc"
# name="notification-frame-17303c6cc" id="webklipper-publisher-widget-container-notification-frame"
# frameborder="0" marginheight="0" marginwidth="0" style="display: block; z-index: 16776272;
# position: fixed; visibility: visible; height: 100%; width: 100%; top: 0px; left: 0px; right: auto;"
# data-notification-layout-id="~184fc0b7" data-notification-layout-name="modal"></iframe>
#   (Session info: chrome=86.0.4240.111)

























































































