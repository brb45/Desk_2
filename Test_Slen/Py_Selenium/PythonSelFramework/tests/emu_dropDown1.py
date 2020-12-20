from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. Handle auto-suggestive drop-down menu
driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.get(url)
# <input data-cy="fromCity" id="fromCity" type="text" class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Del Rio">
driver.find_element_by_id("fromCity").click()

# <input type="text" autocomplete="off" aria-autocomplete="list" aria-controls="react-autowhatever-1" class="react-autosuggest__input react-autosuggest__input--open" placeholder="From" value="">
# fill in textbox, no need to click first ,just use send_keys
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

# <p class="font14 appendBottom5 blackText">Delhi, India</p>
cities = driver.find_elements_by_css_selector("p[class='font14 appendBottom5 blackText']")
time.sleep(5)

# print(len(cities))
driver.implicitly_wait(10)

for city in cities:
    # time.sleep(10)
    if "Del Rio" in city.text:
        print(f"city is {city.text}")
        print(f"class is {city.get_attribute('class')}")
        # city.click()

        # destination_field = driver.find_element(By.XPATH, "//p[text()='Delhi, India']")
        # destination_field.click()
        # break
# 2.



# time.sleep(1)
driver.close()