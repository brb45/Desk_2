from selenium import webdriver
import time

# locator actions
# send_keys("content"), click(), text,clear()
# driver = webdriver.Chrome()
# Same test  cases work on Firefox too.
# No need to change
driver = webdriver.Firefox()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
# time.sleep(1)
print(driver.title)
print(driver.current_url)
assert "ProtoCommerce" == driver.title
assert url == driver.current_url

time.sleep(1)
#@@ 1.find_element_by_name
name = driver.find_element_by_name("name")
print(type(name), "\n", name)
# <class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
# <selenium.webdriver.firefox.webelement.FirefoxWebElement
# (session="8c132f6e-d9bc-4f10-ba59-855dcaf1d613",
# element="6272c0e9-21e1-4fea-a8ab-6682ec224094")>
name.send_keys("Tester")

email = driver.find_element_by_name("email")
print(email)
# (session="8c132f6e-d9bc-4f10-ba59-855dcaf1d613",
# element="6b809b75-6da9-40da-be1e-ef96623aa429")
email.send_keys("ssqa@litepoint.com")

#@@ 2. find element by ID
id = driver.find_element_by_id("exampleCheck1")
print(id)
id.click()
# <selenium.webdriver.firefox.webelement.FirefoxWebElement
# (session="494ec0b4-6bb2-4045-add2-c712035fc2ae",
# element="887aca3e-d3fd-4b1d-93be-d54ad5e3bec5")>

#@@ 3. class name: not recommended since hard to find unique one.
# find_classname = driver.find_element_by_class_name()

#@@ 4. css, need to be unique
# tagname[attribute="value"] --> Tagname optional
# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# input[name='name']
# chrome->Console
# $("input[name='name']")
# java syntax: driver.findElementByName().sendKeys()
time.sleep(2)
find_css = driver.find_element_by_css_selector("input[name='name']")
find_css.clear()
find_css.send_keys("ssqa_test")

#@@ 5. Xpath
# //tagname[@attribute=value] ==> tagname optional
# //input[@type='submit']
# $x("//input[@type='submit']")
# [input.btn.btn-success]
# 0: input.btn.btn-success
# length: 1
# __proto__: Array(0)
xpath1 = "//input[@type='submit']"
xpath  = "//input[@class='btn btn-success']"
find_xpath = driver.find_element_by_xpath(xpath)
find_xpath.click()
## getattribute()
find_xpath.get_attribute(attribute_name)

#@@ 6.
show_text = driver.find_element_by_class_name("alert-success").text
# print(show_text)
# Success! The Form has been submitted successfully!.
assert "succzes" in show_text
#     assert "succzes" in show_text
# AssertionError

#___________________
submit_xpath = "//input[@class='btn btn-success']"
submit_xpath = driver.find_element_by_xpath(submit_xpath)
submit_xpath.click()

css_selector = "div[class='alert alert-success alert-dismissible']"
submit_button = driver.find_element_by_css_selector(css_selector)

text = submit_button.text

if "success!" in text:
    print(True)
if "Success!" in text:
    print("Success!")
# assert "uccesws" in text
#___________________


# customize css_selector tagname[attribute*='value']
# <div class="alert alert-success alert-dismissible">
css_select = "div[class*='alert-success']"
# show_text1  = driver.find_element_by_css_selector(css_select)
# print(show_text1.text)
#
# customize Xpath
# //tagname[contains(@attribute, 'value')]
xpath_custom = "//*[contains(@class, 'alert-success')]"
show_text2 = driver.find_element_by_xpath(xpath_custom)
print(show_text2.text)

time.sleep(5)
driver.close()

## Generate css from ID
# tagname#ID

## xpath text()
# "//tagname[text()= text_string]"
driver.find_element_by_xpath("//a[text()='Cancel']").click()

##
