from selenium import webdriver
import time

# alert
# alert = driver.switch_to.alert
# alert.accept()
# javascript alert

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()
time.sleep(2)

## Switch To Alert Example
# @@ 4. popup
# <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text">
driver.find_element_by_css_selector("#name").send_keys("Alert Test Starts")
time.sleep(5)

# <input id="alertbtn" class="btn-style" value="Alert" onclick="displayAlert()" type="submit">
driver.find_element_by_id("alertbtn").click()

time.sleep(5)
alert = driver.switch_to.alert
print(alert.text)
# alert.accept()
alert.dismiss()
driver.close()