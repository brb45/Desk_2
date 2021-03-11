from selenium import webdriver
import time

# Hide / Show message
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice"
driver.get(url)

# <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
assert driver.find_element_by_id('displayed-text').is_displayed()

driver.find_element_by_id('hide-textbox').click()

assert not driver.find_element_by_id('displayed-text').is_displayed()

# <input id="show-textbox" class="btn-style class2" value="Show" onclick="showElement()" type="submit">
driver.find_element_by_css_selector('#show-textbox').click()
time.sleep(1)


# <input id="alertbtn" class="btn-style" value="Alert" onclick="displayAlert()" type="submit">
alert_button = "//input[@value='Alert']"
alert_xpath  = driver.find_element(By.XPATH, alert_button)
if alert_xpath.is_displayed():
    print('alert_button is present')
# alert_button is present

# alert_xpath.is_enabled()
# alert_xpath.is_selected()
# alert_xpath.is_displayed()

displayed_box = driver.find_element_by_id('displayed-text')
message = "Message shown"
if displayed_box.is_displayed():
    displayed_box.send_keys(message)
if displayed_box.get_attribute('value') == message:
    print(f"{message} is displayed")
# Message shown is displayed




# driver.close()


























































































