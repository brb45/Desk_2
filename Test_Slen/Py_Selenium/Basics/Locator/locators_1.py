from selenium import webdriver
import time

# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://login.salesforce.com"
driver.get(url)
time.sleep(1)
print(driver.title)
print(driver.current_url)

user = "jian.sun@litepoint.com"
passwd = "a1234567"
# <input class="input r4 wide mb16 mt8 username"
# type="email" value="jian.sun@teradyne.com"
# name="username" id="username" aria-describedby="error" style="display: block;">
# css_ = "input[id='username']" same as "input#username"
driver.find_element_by_css_selector("#username").send_keys(user)
time.sleep(1)
# <input class="input r4 wide mb16 mt8 password"
# type="password" id="password"
# name="pw" onkeypress="checkCaps(event)" autocomplete="off">
driver.find_element_by_css_selector(".password").send_keys(passwd)

# driver.find_element_by_css_selector(".password").clear()
time.sleep(2)

# <input class="button r4 wide primary" type="submit" id="Login" name="Login" value="Log In">
login = "#Login"
driver.find_element_by_css_selector(login).click()
time.sleep(2)


#@@ locator: link_text
# <a id="forgot_password_link" class="fl small" href="/secur/forgotpassword.jsp?locale=us">Forgot Your Password?</a>
# driver.find_element_by_link_text("Forgot Your Password?").click()
# time.sleep(3)

#@@ 1. Generate css from class name
# tagname.class_name
# make sure no space in class name, replace space with .

#@@ 2. Generate xpath based on text, text is case-sensitive
# <a href="/" class="secondary button fiftyfifty mb16">Cancel</a>
# //tagname[text()='xxx']
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//a[text()='cancel']"}
# driver.find_element_by_xpath("//a[text()='Cancel']").click()
# time.sleep(3)

#@@3. Create Xpath and CSS by Traversing Tags
# xpath: ParentTag/ChildTag
# css:   ParentTag ChildTag

#@@4. Select Parent Locator from Child using Xpath
# Xpath/parent::tagName

# driver.close()

























































































