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
# CSS Selectors by Attribute
# Let’s imagine we have a tag with the following attributes [id, class, name, value]
#
# <input type="text" id="fistname" name="first_name" class="myForm">
# The generic way to locate elements by attribute is:
#
# css = "element_name[<attribute_name> = '<value>']"
# Example:
#
# WebElement firstName = driver.findElement(By.cssSelector("input[name='first_name']"));

## 1. Id Attribute
# In CSS, we can use # notation to select the id attribute of an element:
#
# driver.findElement(By.cssSelector("input#firstname"));
# //or
# driver.findElement(By.cssSelector("#firstname"));

## 2. Class Attribute
# Class is not unique as ID.
# dot(.) refers to class
# The same principle can be used to locate elements by their class attribute.
# We use the . notation.
# driver.findElement(By.cssSelector("input.myForm"));
#
# //or
#
# driver.findElement(By.cssSelector(".myForm"));
# Note: Take extra care when using the . notation as there could be
# many web elements on the HTML source with the same class attribute.

##2.1
# For example if the below is the html for a sign button
#
"""
<button class="submit btn primary-btn flex-table-btn js-submit" type="submit" style="background-color: rgb(85, 172, 238);">
 Log in
</button>
"""
# In the above html there are multiple classes used for the single button.
# How to work in such a situation????
# Below are the examples to work with classes.
# If you observe, we have combined multiple classes to work.
# As the class is not unique like ID, we may require to join two classes and find the accurate element.

# The CSS class selector matches elements based on the contents of their class attribute.
# In the below exampleprimary-btn is class attribute value.
#
# Example 1: css=.primary-btn
# Example 2: css=.btn.primary-btn
# Example 3: css=.submit.primary-btn
# The above can be written like below in selenium
#
# WebElement ele1 = driver.findElement(By.cssSelector(".primary-btn"));
# WebElement ele2 = driver.findElement(By.cssSelector(".btn.primary-btn"));
# WebElement ele3 = driver.findElement(By.cssSelector(".submit.primary-btn"));

## 3. Multiple Attributes
# Sometimes there is a need to be more specific with the selection criteria in order to locate the correct element.
#
# <div class="ajax_enabled" style="display:block">
# The value of the display could either be “none” or “block” depending on the ajax call.
# In this situation, we have to locate the element by both class and style.
#
# driver.findElement(By.cssSelector("div[class='ajax_enabled'] [style='display:block']"));

## 4. Attribute NOT contain a specific value
# In WebDriver, how do you find elements whose attribute contain values
# which you don’t want to select?
#
# <div class="day past  calendar-day-2017-02-13 calendar-dow-1 unavailable">
# <div class="day today calendar-day-2017-02-14 calendar-dow-2 unavailable">
# <div class="day       calendar-day-2017-02-15 calendar-dow-3">
# <div class="day       calendar-day-2017-02-16 calendar-dow-4">

# In the above snippet, we want to select an available day (i.e. the two last div elements)
# As can be seen, all four divs contain “calendar-day-“ but the first two also contain “unavailable” which we don’t want.

# The CSS selector for Not selecting the first two divs is
#
# driver.findElement(By.cssSelector("div[class*='calendar-day-']:not([class*='unavailable'])"));"

## 5. Locating Child Element
# <div id="logo">
#     <img src="./logo.png" />
# </div>

# To locate the image tag, we use:
# driver.findElement(By.cssSelector("div#logo img"));

## 5.1 Multiple Child Elements
# There are occasions when there are multiple child elements
# within the same parent element such as list elements
#
# <ul id="fruit">
#     <li>Apple</li>
#     <li>Orange</li>
#     <li>Banana</li>
# </ul>
# As can be seen, the individual list elements don’t have any id
# associated with them. To locate the element with text ‘Orange’,
# we have to use nth-of-type.
#
# Example:

# driver.findElement(By.cssSelector("ul#fruit li:nth-of-type(2)"));
# driver.findElement(By.cssSelector("ul#fruit>li:nth-of-type(2)"));

# Likewise, to select the last child element, i.e. ‘Banana’, we use:

# driver.findElement(By.cssSelector("ul#fruit li:last-child"));




##---------------------------------------------------
# In this example, all the three div elements contain the word ‘random’.
#
# <div id="123_randomId">
# <div id="randomId_456">
# <div id="123_pattern_randomId">

## 6. Attribute Starts with
# To select the first div element, we would use ^= which means ‘starts with’:
#
# driver.findElement(By.cssSelector("div[id^='123']"));

## 7. Attribute Ends with
# To select the second div element, we would use $= which means ‘ends with’:
#
# driver.findElement(By.cssSelector("div[id$='456']"));

## 8. Attribute Contains
# To select the last div element we would use *= which means ‘sub-string’
#
# driver.findElement(By.cssSelector("div[id*='_pattern_']"));
# We can also use the contains
#
# driver.findElement(By.cssSelector("div:contains('_pattern_')"));
#---------------------------------------









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

























































































