from selenium import webdriver
from datetime import datetime
import time

# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# driver.get(url)


#name
# url = "https://login.salesforce.com"
# driver = webdriver.Chrome()
# driver.get(url)
#
# name.send_keys("Tester")
# time.sleep(2)
# print(name.text)
# email = driver.find_element_by_name("email")
# print(email)
# # (session="8c132f6e-d9bc-4f10-ba59-855dcaf1d613",
# # element="6b809b75-6da9-40da-be1e-ef96623aa429")
# email.send_keys("ssqa@litepoint.com")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
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

#__________________________________________________
driver = webdriver.Chrome()
url =  "https://www.makemytrip.com/"
driver.get(url)
driver.maximize_window()

element = driver.find_element_by_id("fromCity")
time.sleep(1)
element.send_keys("del")
time.sleep(1)

## find_elements NOT find_element
city_list = driver.find_elements_by_css_selector("p[class='font14 appendBottom5 blackText']")
print(f"num of cities is {len(city_list)}")
for c in city_list:
    print(c.text)
    if c.text  == "Delhi, India":
        print(c.text)  #Delhi, India
        c.click()
        time.sleep(2)
        break
time.sleep(1)
# <input data-cy="toCity" id="toCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Bangalore">
desti = driver.find_element_by_id("toCity")
time.sleep(1)
# desti.click()
time.sleep(1)
# <p class="font14 appendBottom5 blackText">Pune, India</p>
destination = driver.find_element_by_xpath("//p[text()='Pune, India']")
destination.click()
time.sleep(2)
# selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:













# driver.quit()


