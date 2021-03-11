from selenium import webdriver
from datetime import datetime
import time


# Selenium.common.exceptions.NoSuchElementException


url = "https://login.salesforce.com"
driver = webdriver.Chrome()
driver.get(url)

# <input class="input r4 wide mb16 mt8 username" type="email" value="" name="username" id="username" aria-describedby="error" style="display: block;">
username = driver.find_element_by_name("username")
print(username)
print(driver.session_id)
# <selenium.webdriver.remote.webelement.WebElement
# (session="  73b57fd3b450885dee3e9abe92447593", element="d674d5c2-e9b2-4148-a194-3f812192222c")>
# Session_id: 73b57fd3b450885dee3e9abe92447593
username.send_keys("ssqa@litepoint.com")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# seems that class name can't have space in between
# class_selector = "form-control ng-pristine ng-invalid ng-touched"
# class_name = driver.find_element_by_class_name(class_selector)
# class_name.send_keys("Warrior")
# selenium.common.exceptions.NoSuchElementException:
# Message: Unable to locate element: .btn btn-success
#__________________________________________________
#
#
# user = "jian.sun@litepoint.com"
# passwd = "Ssqatest1"

# # <input class="input r4 wide mb16 mt8 username"
# # type="email" value="jian.sun@teradyne.com"
# # name="username" id="username" aria-describedby="error" style="display: block;">

# driver.find_element_by_css_selector("#username").send_keys(user)
# # <input class="input r4 wide mb16 mt8 password"
# # type="password" id="password"
# # name="pw" onkeypress="checkCaps(event)" autocomplete="off">
# driver.find_element_by_css_selector(".password").send_keys(user)
# time.sleep(2)
# driver.find_element_by_css_selector(".password").clear()
# time.sleep(2)
#
#
# #@@ locator: link_text
# # <a id="forgot_password_link" class="fl small" href="/secur/forgotpassword.jsp?locale=us">Forgot Your Password?</a>
# driver.find_element_by_link_text("Forgot Your Password?").click()
# time.sleep(3)
#
# driver.find_element_by_xpath("//a[text()='Cancel']").click()
# time.sleep(3)



# driver.quit()


