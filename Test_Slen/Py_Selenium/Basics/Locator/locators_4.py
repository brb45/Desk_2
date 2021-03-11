from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
# radio button
# button.is_displayed()
# button.is_enabled()
# button.is_selected()


driver = webdriver.Chrome()

url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

time.sleep(1)
# @@ 3. radio
# <input value="radio1" name="radioButton" class="radioButton" type="radio">
xpath_sel = "//input[@type='radio']"
radio_button = driver.find_elements_by_xpath(xpath_sel)

for button in radio_button:
    if button.get_attribute('value') =='radio2':
        button.click()
        assert button.is_selected()
        print(f'button.is_displayed() is {button.is_displayed()}')
        print(f'button.is_enabled() is {button.is_enabled() }')
        print(f'button.is_selected() is {button.is_selected()} ')

        # button.is_displayed() is True
        # button.is_enabled() is True
        # button.is_selected() is True


time.sleep(2)
radio_button_3 = "//input[@value='radio3']"
driver.find_element_by_xpath(radio_button_3).click()







time.sleep(2)
driver.close()


























































































