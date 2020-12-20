from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
# radio button

# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()
time.sleep(2)
# @@ 3. radio
# <input value="radio1" name="radioButton" class="radioButton" type="radio">
xpath_sel = "//input[@type='radio']"
radio_button = driver.find_elements_by_xpath(xpath_sel)

for button in radio_button:
    if button.get_attribute('value') =='radio2':
        button.click()
        assert button.is_selected()
        print(True)

time.sleep(2)
radio_button_3 = "//input[@value='radio3']"
driver.find_element_by_xpath(radio_button_3).click()







time.sleep(2)
driver.close()


























































































