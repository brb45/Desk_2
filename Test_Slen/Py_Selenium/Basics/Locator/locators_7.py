from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
# alert = driver.switch_to.alert
# alert.accept()
# Java, javascript alert
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

## Switch To Alert Example
# @@ 4. popup
# <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text">
driver.find_element_by_css_selector("#name").send_keys("Send Alert")
time.sleep(2)

# <input id="alertbtn" class="btn-style" value="Alert" onclick="displayAlert()" type="submit">
driver.find_element_by_id("alertbtn").click()

time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()


# <input id="confirmbtn" class="btn-style" value="Confirm" onclick="displayConfirm()" type="submit">
xpath = "//input[@onclick='displayConfirm()']"
confirmation = driver.find_element_by_xpath(xpath).click()

time.sleep(1)
confirm = driver.switch_to.alert
print(confirm.text)
confirm.dismiss()
# confirm.accept()

# selenium.common.exceptions.UnexpectedAlertPresentException:
# Alert Text: Hello Send Alert, share this practice page and share your knowledge
# Message: unexpected alert open: {Alert text : Hello Send Alert, share this practice page and share your knowledge}
#   (Session info: chrome=86.0.4240.111)


time.sleep(5)
driver.close()


























































































