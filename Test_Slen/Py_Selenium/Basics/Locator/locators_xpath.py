from selenium import webdriver
import time

# locator actions
# send_keys("content"),
# click(),
# text,
# clear()

# driver actions
# driver.title
# driver.get()
# driver.current_url


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://login.salesforce.com"
driver.get(url)
time.sleep(1)

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

#--------------------------------------


























































































