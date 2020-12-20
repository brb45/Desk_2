# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# # Navigate to url
# driver.get("http://www.example.com")
#
# driver.add_cookie({"name": "test1", "value": "cookie1"})
# # driver.add_cookie({"name": "test2", "value": "cookie2"})
#
# # Get all available cookies
# print(driver.get_cookies())
# print("-------------------")
# print(driver.get_cookie("name"))


from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})
driver.add_cookie({"name": "test", "value": "QA"})

# Get cookie details with named cookie 'foo'
print(type(driver.get_cookies()))
print(driver.get_cookies())
# <class 'list'>
# [{'domain': 'www.example.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': False, 'value': 'bar'}]

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))
print(type(driver.get_cookie("foo")))

# <class 'dict'>
# {'domain': 'www.example.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': False, 'value': 'bar'}

# Delete a cookie with name 'foo'
driver.delete_cookie("foo")

print(driver.get_cookies())
# [{'domain': 'www.example.com', 'httpOnly': False, 'name': 'test', 'path': '/', 'secure': False, 'value': 'QA'}]

#  Deletes all cookies
driver.delete_all_cookies()

print(driver.get_cookies()) # []

print(driver.get_cookie("foo"))  # None