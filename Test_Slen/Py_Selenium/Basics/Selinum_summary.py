## xpath, css_selector
from selenium import webdriver

driver = webdriver.Chrome()

#------------------------------------------------
find_css = driver.find_element_by_css_selector("input[name='name']")

# name="username" id="username" aria-describedby="error" style="display: block;">
driver.find_element_by_css_selector("#username").send_keys(user)

driver.find_elements_by_css_selector("p[class*='blackText']")

#------------------------------------------------
#@@ 1. Generate css from class name
# tagname.class_name
# make sure no space in class name, replace space with .

xpath1 = "//input[@type='submit']"
xpath  = "//input[@class='btn btn-success']"
find_xpath = driver.find_element_by_xpath(xpath)

xpath_custom = "//*[contains(@class, 'alert-success')]"

# <a href="/" class="secondary button fiftyfifty mb16">Cancel</a>
driver.find_element_by_xpath("//a[text()='Cancel']").click()

##1. wait
# implicitly_wait vs explicit_wait

##2. DOM

##3. presence of element located vs visibility of element located

## 4.
# Best Practices For Using Locators In Selenium WebDriver
# Keeping in mind which locator to choose is as important as ensuring you know all the locators.
# Certain best practices and rules have been laid down to ensure you make efficient use of locators in Selenium WebDriver.
# Listing few below:
#
# Do not locate elements that depends on information which may change as they may make your locators
# easy to break and less maintainable.
# This is one of the key rules that one needs to keep in mind while writing better automation code
# using locators in Selenium WebDriver. If locator is dependent on a single entity like for instance class, name, id etc which if changed may need to be repaired but in case of complex locators like By.XPath(“//div[@class=”class-form_6180″]/div[5]/h3”), it may lead to frequent breakage if any of the div’s changes or the class name etc. Try to make your locators in Selenium WebDriver precise and dependent on single entity than multiple. Only in case you do not have any option left, move to complex locators, but make sure the dependent elements have less likelihood of changing.
#
# Ensure your locator In Selenium matches only the required information to be selected and
# not multiple other information present along with it.
# This is contextual and depends upon your scenario. In case you wish to locate single element,
# ensure it matches uniquely to only one element. It should never be the case, where there are multiple elements
# identified via locator and you opt to choose for the second or third selection. This can be a point of
# your script breakage, since if the page design changes or the assumed count on which the selected element appears changes,
# your locator will tend to break. So always make sure, your locator locates the exact match.

# Secondly, if you are trying to look out for multiple matches (using ‘findElements’),
# ensure it matches all the desired elements you are looking out for.

# While using locators in Selenium, do not locate elements that depend on auto-generated values.
# When new to this business this is something we get into. Usually ID’s are auto generated and while locating them and using them in scripts could be problematic. Every time the script or page containing those ID’s are run they tend to change and make your scripts fail. The easiest solution to figure out whether they are auto generated or not is watching them through minimum 2 runs and identifying them through the prefix/post fixed number associated with it. In case they are changed or incremented, you can conclude those are auto generated and you look out for other ways to locate those elements.



# While choosing locators of Selenium, do not use XPath or CSS Selector provided by the Dev Tools.
# Yes, you read that right! Copying xpath or css selector from developer tools is something
# we believe is the easiest task to do, but believe me these are one of the problems
# that appears in the longer run, causing problems in the stability and readability of your scripts.
# Your browser providing you these values does not look out for meaningful XPath
# or CSS locators and give you complex ones, with multiple dependent factors,
# which I mentioned above may lead to frequent breakages.
# So even though this may look tempting and easier to do activity try refraining yourself from it.

# These are some of the factors one should keep in mind while writing locators in Selenium WebDriver.
# The technique or strategy you use to locate elements can be any but make sure the above rules
# are fulfilled which helps to make your script easy to maintain and read.
# These locators in Selenium are the building blocks of your script,
# make sure they are correct and your road ahead on it is smoother and more focused towards other
# aspects of the functionality of your project as you automate them.


## 5. DOM vs HTML
# The Document Object Model (DOM) is a language-independent model,
# made up of objects representing the structure of a document. HTML is one language for writing such documents.

# DOM is the tree model to represent HTML.

#  for example, have a html page and add a tag with javascript.
# The actual HTML of the page is still the same, but the "DOM" however has changed.

# The HTML of a page is a string, and the DOM of the page is what happens when you take that
# string and construct an object in the object-oriented programming sense of the term "object".
# Creating that object is how JavaScript is able to interact with the page:
#
# https://en.wikipedia.org/wiki/Document_Object_Model#JavaScript

# When a web page is loaded, the browser creates a Document Object Model of the page,
# which is an object oriented representation of an HTML document,
# that acts as an interface between JavaScript and the document itself and allows the creation of dynamic web pages.

# HTML is what comes back from the server in the answer request,
# gets parsed and the DOM (= Document Object Model) is what the browser builds with it
# and can be manipulated with JavaScript. This makes a huge difference if you miss an element from a web page.
# Where should you look for it?

# Elements that are gone in the DOM (=Inspector) but are present in the HTML from the server
# must have been deleted by JavaScript. Here are some basic questions i will ask junior developer

# if an element is missing in a page:
# Look at the DOM first, is the element there?
# Is the element visible in the DOM with CSS display property and z-index?
# Is the element in the HTML or was build with JavaScript?

# If it’s build with JavaScript then search in the source tab in the Developer Tools for
# parts of the class name to find a close line in JS where it may be generated.
