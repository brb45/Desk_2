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
driver.quit()
#--------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.unixtimestamp.com/"
driver = webdriver.Chrome()
driver.get(url)

time_loc = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/h3[2]"
time_loc1 = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/h3[2]"
time_stmp = driver.find_element_by_xpath(time_loc)
print(time_stmp.text)
# driver.quit()

# 1610498741 seconds since Jan 01 1970. (UTC)
url = "http://random-name-generator.info/"
driver.get(url)
# xpath_loc = '//*[@id="main"]/div[3]/div[2]/ol//li'
# xpath_loc = '//div[@id="main"]/div[3]/div[2]/ol//li'
xpath_loc = '//div[@id="main"]/div[3]/div[2]/ol/li[1]'
# names = driver.find_elements(By.XPATH, xpath_loc)
loc_type = By.XPATH
names = driver.find_elements(loc_type, xpath_loc)
print(type(names)) # <class 'list'>
for name in names:
    print(name.text)

#

























































































