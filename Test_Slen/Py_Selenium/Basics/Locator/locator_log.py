from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
driver = webdriver.Chrome(options=options)




# options = webdriver.ChromeOptions()
# options.add_argument('ignore-certificate-errors')
#
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://cacert.org/')
#
# driver.close()

url = ""
# driver = webdriver.Chrome()

url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

print(driver.title)
print(driver.current_url)
# assert "ProtoCommerce" == driver.title
# assert url == driver.current_url

loc_name = 'name'
name = driver.find_element_by_name(loc_name)
name.send_keys("Tester")
print("type is ", type(name))
# type is  <class 'selenium.webdriver.remote.webelement.WebElement'>
print("name is ",  name)
# name is  <selenium.webdriver.remote.webelement.WebElement
# (session="94fa27fad67123e5ae7c85c929ef9b4e", element="02ed17af-de1a-416d-913c-b10ada98077b")>

email = driver.find_element_by_name("email")
email.send_keys('ssqa@litepoint.com')
print("email is ", email)
# email is  <selenium.webdriver.remote.webelement.WebElement
# (session="8857d3be73a46388386244b14b30e8e7", element="fd4c8122-59a0-4757-a197-f74c6907bfb5")>
id = driver.find_element_by_id("exampleCheck1")
id.click()

#
# #@@ 3. class name: not recommended since hard to find unique one.
# # find_classname = driver.find_element_by_class_name()
#
# #@@ 4. css, need to be unique
# # tagname[attribute="value"] --> Tagname optional
# # <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">

# # input[name='name']

find_css = driver.find_element_by_css_selector("input[name='name']")
find_css.clear()
find_css.send_keys("ssqa_test")
#
# #@@ 5. Xpath
# # //tagname[@attribute=value] ==> tagname optional
# # //input[@type='submit']
# # $x("//input[@type='submit']")
# # [input.btn.btn-success]
# # 0: input.btn.btn-success
# # length: 1
# # __proto__: Array(0)

# xpath1 = "//input[@type='submit']"
xpath  = "//input[@class='btn btn-success']"
find_xpath = driver.find_element_by_xpath(xpath)
find_xpath.click()
# ## getattribute()
# find_xpath.get_attribute(attribute_name)
#
# #@@ 6.
# <div class="alert alert-success alert-dismissible">
#                     <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#                     <strong>Success!</strong> The Form has been submitted successfully!.
# </div>

# import time
# time.sleep(3)
# NOT WORKING
# alert = driver.find_element_by_class_name("alert alert-success alert-dismissible")
# alert_text = alert.text
# print(alert_text)

css_selector = "div[class='alert alert-success alert-dismissible']"
alert_message = driver.find_element_by_css_selector(css_selector)
text = alert_message.text
print(text)
print("-------------------------------")
#
# if "success!" in text:
#     print(True)
# if "Success!" in text:
#     print("Success!")
# assert "uccesws" in text
# #___________________
#
#
# customize css_selector tagname[attribute*='value']
# <div class="alert alert-success alert-dismissible">
css_select = "div[class*='alert-success']"
show_text1  = driver.find_element_by_css_selector(css_select)
print(show_text1.text)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# #
# # customize Xpath
# # //tagname[contains(@attribute, 'value')]
xpath_custom = "//*[contains(@class, 'alert-success')]"
show_text2 = driver.find_element_by_xpath(xpath_custom)
print(show_text2.text)
print("**************************")
#



# NOT working
xpath_1 = "//*[contains(text(),'successful')]"
# show_text3 = driver.find_element_by_xpath(xpath_1)
# print(show_text3.text)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
time.sleep(5)
driver.close()
#
# ## Generate css from ID
# # tagname#ID
#
# ## xpath text()
# # "//tagname[text()= text_string]"
# driver.find_element_by_xpath("//a[text()='Cancel']").click()
#
# ##
