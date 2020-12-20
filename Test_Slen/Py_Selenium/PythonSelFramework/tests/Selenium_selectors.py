from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


#css
# tagName is optional
# tagName[attribute='value']

# tagName[attribute*='value']
# tagName#id_value  for id attribute

# Generate css from classname
# tagname.classname_1.classname_2

#Xpath
# //tagName[@attribute='value']
# //tagName[contains(@attribute, 'value')]
# //tagname[text()="values"]
# text_field = driver.find_element_by_xpath("//[text()='Your content goes here.']")

# xpath: array: index start from 1
# url = "https://en.wikipedia.org"
# Logo = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/a')
# logo = driver.find_element(*Logo)


# create xpath and css by traversing tags
# xpath: valid_Parent_xpath/ChildTag
# css: valid_parent_css childTag

# Select Parent locator from child using Xpath
# xpath/parent::tagname

# path index starts with 1
# in dropdowm menu, select_by_index, the index start with 0

driver = webdriver.Chrome()
url = "https://login.salesforce.com/"
driver.get(url)

# <form name="login" method="post" id="login_form" onsubmit="handleLogin();" action="https://login.salesforce.com/"
# target="_top" autocomplete="off" novalidate="novalidate"><fieldset style="display:none">
# <div id="usernamegroup" class="inputgroup"><label for="username" class="label usernamelabel">Username</label>
# <a id="hint_back_chooser" href="#" onclick="LoginHint.showChooser(); return false;" class="fr small">1 Saved Username</a>
# <div id="username_container"><div id="idcard-container" class="mt8 mb16" style="display: none;">
# <div id="idcard" aria-label="jian.sun@litepoint.com"><img id="idcard-avatar" class="avatar" alt="
# " src="https://litepoint.my.salesforce.com/img/userprofile/default_profile_45_v2.png" title="jian.sun@litepoint.com">
# <a href="javascript:void(0);" id="clear_link" class="clearlink" onclick="LoginHint.clearExistingIdentity();">
# <img alt="Log In with a Different Username" class="clearicon" src="/img/clear.png"></a>
# <span id="idcard-identity">jian.sun@litepoint.com</span></div></div><input class="input r4 wide mb16 mt8 username" type="email" value="" name="username" id="username" aria-describedby="error" style="display: block;"><input type="hidden" name="ExtraLog" value="%5B%7B%22width%22:1920%7D,%7B%22height%22:1200%7D,%7B%22language%22:%22en-US%22%7D,%7B%22offset%22:8%7D,%7B%22scripts%22:%5B%7B%22size%22:249,%22summary%22:%22if%20(self%20==%20top)%20%7Bdocument.documentElement.style.v%22%7D,%7B%22size%22:528,%22summary%22:%22var%20SFDCSessionVars=%7B%5C%22server%5C%22:%5C%22https:%5C%5C/%5C%5C/login.sal%22%7D,%7B%22url%22:%22https://login.salesforce.com/jslibrary/SfdcSessionBase208.js%22%7D,%7B%22url%22:%22https://login.salesforce.com/jslibrary/LoginHint208.js%22%7D,%7B%22size%22:26,%22summary%22:%22LoginHint.hideLoginForm();%22%7D,%7B%22size%22:36,%22summary%22:%22LoginHint.getSavedIdentities(false);%22%7D,%7B%22url%22:%22https://login.salesforce.com/jslibrary/baselogin.js%22%7D,%7B%22url%22:%22https://login.salesforce.com/marketing/survey/survey1/1384%22%7D,%7B%22url%22:%22https://login.salesforce.com/marketing/survey/survey4/1384%22%7D,%7B%22size%22:357,%22summary%22:%22function%20handleLogin()%7Bdocument.login.un.value=doc%22%7D%5D%7D,%7B%22scriptCount%22:10%7D,%7B%22iframes%22:%5B%22https://c.salesforce.com/login-messages/promos.html%22,%22https://login.salesforce.com/login/sessionserver212.html%22%5D%7D,%7B%22iframeCount%22:2%7D,%7B%22referrer%22:%22NO_REFERRER%22%7D%5D"><input type="hidden" name="Fingerprint" value="%7B%22platform%22:%22Win32%22,%22window%22:%221160x1920%22,%22screen%22:%221200x1920%22,%22color%22:%2224-24%22,%22timezoneOffset%22:%22480%22,%22canvas%22:%22-809163694%22,%22sessionStorage%22:%22true%22,%22LocalStorage%22:%22true%22,%22indexDB%22:%22true%22,%22webSockets%22:%22true%22,%22plugins%22:%22Chrome%20PDF%20Plugin:Portable%20Document%20Format%5CnChrome%20PDF%20Viewer:%5CnNative%20Client:%5Cn%22,%22drm%22:1,%22languages%22:%5B%22en-US%22,%22en%22,%22fr%22,%22la%22%5D,%22fonts%22:%22%22,%22codecs%22:%22gIEIqgoIQqoCqH4=%22,%22mediaDevices%22:%22audioinput::default%5Cnaudioinput::communications%5Cnaudioinput::be42d17772bd28635526abd6b3e099dc0ecaa1fe844253723172e5ef11a1ed9b%5Cnvideoinput::05d06b4c4fd3610c1134e848a480b996e9c209292bafec6c2aa8f083f6dba5a3%5Cnaudiooutput::default%5Cnaudiooutput::communications%5Cnaudiooutput::1a5ae78ba167e99f7d3a0fe59c2ae745579981c481f09873d906a0aeca4713d9%5Cnaudiooutput::2df71a661a71ffeca7c3e9f855b1269809f8969cd3234ec879dff1b7504a29a5%5Cnaudiooutput::d95c556ba42deae0885e83e6af0b9227142be9dc1b95fbe3953bfceda586c087%5Cn%22%7D"></div></div><label for="password" class="label">Password</label><input class="input r4 wide mb16 mt8 password" type="password" id="password" name="pw" onkeypress="checkCaps(event)" autocomplete="off"><div id="pwcaps" class="mb16" style="display:none"><img id="pwcapsicon" alt="Caps Lock is on." width="12" src="/img/icon/capslock_blue.png"> Caps Lock is on.</div><input class="button r4 wide primary" type="submit" id="Login" name="Login" value="Log In"><div class="w0 pr ln3 p16 remember"><input type="checkbox" class="r4 fl mr8" style="" id="rememberUn" name="rememberUn"><label for="rememberUn" class="fl pr db tn3">Remember me</label><br></div></form>
xpath_child =      "//form[@name='login']/div[1]/label"
css_selector_child = "form[name='login'] div[1] label"
#if labels have children
css_grandchild = "form[name='login'] label:nth-child(1)"
# xp_1 = driver.find_element(By.XPATH, xpath_child)
# print(xp_1.text) # Username
css_1 = driver.find_element(By.CSS_SELECTOR, css_grandchild)

print(f"css_grandchild is {css_1.text}")
# print(f"xpath_child is  {driver.find_element_by_xpath(xpath_child).text}")
# print(f"css_selector_child is  {driver.find_element_by_css_selector(css_selector_child).text}")

# NOSuchElementException
# div[] starts  with div[0]
xpath_username = driver.find_element_by_xpath("//form[@name='login']/div[1]/label")
print(f"xpath_username is {xpath_username.text}") #  xpath_username is Username

xpath_passwd = driver.find_element_by_xpath("//form[@name='login']/label")
print(f"xpath_username is {xpath_passwd.text}") # xpath_username is Password

# <input class="input r4 wide mb16 mt8 password" type="password" id="password" name="pw" onkeypress="checkCaps(event)" autocomplete="off">
xpath_pwd_input  = driver.find_element_by_xpath("//form[@name='login']/input")
print(f"xpath_pwd_input is {xpath_pwd_input.get_attribute('id')}") # xpath_pwd_input is password
xpath_name = driver.find_element_by_name("pw")
print(f"xpath_name is {xpath_name.get_attribute('name')}") # xpath_name is pw

# <input class="button r4 wide primary" type="submit" id="Login" name="Login" value="Log In">
xpath_rem = driver.find_element_by_xpath("//form[@name='login']/div[3]/input")
print(f"xpath_rem is {xpath_rem.get_attribute('id')}") # xpath_rem is rememberUn
time.sleep(1)
driver.close()