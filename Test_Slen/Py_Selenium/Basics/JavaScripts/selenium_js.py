from selenium import webdriver

driver = webdriver.Chrome()
# Syntax –

# execute_script(script, *args)
# Args –
# script: The JavaScript to execute.
# *args: Any applicable arguments for your JavaScript.

# run javascript
driver.execute_script("some Javascript code here")

# There are two ways we can execute JavaScript within the browser.

#   Method 1: Executing JavaScript at Document Root Level
# In this case, we capture the element that we want to work with,
# using JavaScript-provided methods, then declare some actions on it
# and execute this JavaScript using WebDriver.

#   Notice [0]   in the getElementsByName('username')[0]  statement above.
# JavaScript functions getElementsByName ,  getElementsByClassName ,
# and so on return all matching elements as an array.
#
# In our case, we need to act on the first matching element that can be accessed
# via  index [0] . If you know what you are doing, i.e.,
# if you know the index of the element you want to operate, you can directly use the index,
# such as  getElementsByName('username')[2] .

# However, if you are using the JavaScript function ' getElementById ',
# you do not need to use any indexing, as it will return only one element (‘id’ should be unique).

# getElementsByName
# getElementsByClassName
# getElementById
javaScript = "document.getElementsByName('username')[0].click();"
driver.execute_script(javaScript)

# **********  Method 2: Executing JavaScript at Element Level
userName = driver.find_element_by_xpath("//button[@name='username']")
driver.execute_script("arguments[0].click();", userName)

# his operation in a single line of code:
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# That means the  execute_script()  method can return values.
print(driver.execute_script('return document.getElementById("fsr").innerText'))

# Summary
# Here is a summary of a few potential actions for which JavaScript could be used.
#
# get elements text or attribute
#
# find an element
#
# do some operation on an element, like click()
#
# change attributes of an element
#
# scroll to an element or location on a web page
#
# wait until the page is loaded

