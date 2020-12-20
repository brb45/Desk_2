from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://login.salesforce.com/"
driver.get(url)

# <input class="input r4 wide mb16 mt8 username" type="email" value="" name="username" id="username" aria-describedby="error" style="display: block;">
driver.find_element_by_css_selector("#username").send_keys("jian.sun@litepoint.com")

# <input class="input r4 wide mb16 mt8 password" type="password" id="password" name="pw" onkeypress="checkCaps(event)" autocomplete="off">
driver.find_element_by_css_selector("#password").send_keys("wu")
# driver.find_element_by_css_selector("#password").clear()

# <input class="button r4 wide primary" type="submit" id="Login" name="Login" value="Log In">
driver.find_element_by_name("Login").submit()
#
# # <a id="forgot_password_link" class="fl small" href="/secur/forgotpassword.jsp?locale=us">Forgot Your Password?</a>
# # driver.find_element_by_link_text("Forgot Your Password?").click()
# driver.find_element_by_xpath("//a[text()='Forgot Your Password?']").click()
# time.sleep(3)
# # <a href="/" class="secondary button fiftyfifty mb16">Cancel</a>
# # https://login.salesforce.com/secur/forgotpassword.jsp?locale=us
# driver.find_element_by_xpath("//a[text()='Cancel']").click()

time.sleep(5)
driver.close()