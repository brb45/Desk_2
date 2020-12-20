from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. Handle auto-suggestive drop-down menu
driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.implicitly_wait(10)
driver.get(url)

# <input data-cy="fromCity" id="fromCity" type="text" class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Del Rio">
# driver.find_element_by_id("fromCity").click()
driver.find_element_by_id("fromCity").send_keys('del')
# time.sleep(1000)
# <p class="font14 appendBottom5 blackText">Delhi, India</p>
from_city = driver.find_element_by_xpath("//p[text()='Delhi, India']")
print(f"from {from_city.text}")
time.sleep(20)
from_city.click()


# <input type="text" autocomplete="off" aria-autocomplete="list"
# aria-controls="react-autowhatever-1"
# class="react-autosuggest__input react-autosuggest__input--open" placeholder="To" value="">

driver.find_element_by_css_selector("input[placeholder='To']").send_keys("mu")

# <p class="font14 appendBottom5 blackText">Del Rio, United States</p>
# <p class="font14 appendBottom5 blackText">Mumbai, India</p>
to_city = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
print(f"to_city: {to_city.text}")
to_city.click()
# <div class="DayPicker-Day DayPicker-Day--selected" tabindex="-1" role="gridcell"
# aria-label="Fri Nov 13 2020" aria-disabled="false" aria-selected="true">
#   <div class="dateInnerCell">
#       <p>6</p>
#   </div>
# </div>
date_field = driver.find_element_by_xpath("//div[@aria-label='Fri Nov 13 2020']/div/p")
print(date_field.text)
date_field.click()
# from Delhi, India
# to_city: Mumbai, India
# 6

# 2.

time.sleep(1000)
driver.close()