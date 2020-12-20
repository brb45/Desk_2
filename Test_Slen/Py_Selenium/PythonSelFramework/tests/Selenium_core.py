from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import  selenium
driver = webdriver.Chrome()
# url = "https://rahulshettyacademy.com/angularpractice/"
# print(f"selenium.__version__  is {selenium.__version__}") #  3.141.0
# driver.maximize_window()
# driver.get(url)

# 1. click on link
# Verify with some typical element in the new page

url  = "https://rahulshettyacademy.com/angularpractice"
# driver.get(url)
# <a class="nav-link" href="/angularpractice/shop">Shop</a>
# print(driver.current_url)
# shop_item = driver.find_element(By.LINK_TEXT, "Shop")
# shop_item = driver.find_element(By.PARTIAL_LINK_TEXT, "Sh")
# shop_item = driver.find_element(By.CSS_SELECTOR, 'a[href*="/shop"]')
# shop_name = driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")

# shop_item = driver.find_element(By.XPATH, "//a[contains(@href,'shop')]")
# shop_item.click()
# <h1 class="my-4">Shop Name</h1>
# page_verify = driver.find_element_by_class_name("my-4")
# print("Shop Name" in page_verify.text )
# print(driver.current_url)
# https://rahulshettyacademy.com/angularpractice/shop
#

# 2. send_keys(text_field)
# Verified with get_attribute("value")

# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-untouched ng-pristine ng-invalid'")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input.form-control.ng-untouched.ng-pristine.ng-invalid")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[class*='ng-invalid'")
# name_text_field = driver.find_element(By.XPATH, "//input[@name='name']")
# name_text_field = driver.find_element(By.XPATH, "//input[@minlength='2']")

# name_field = driver.find_element(By.NAME, "name")
# name_field.send_keys("ssqa_ssqaaa")
# page_verify = name_field.get_attribute("value") == "ssqa_ssqaaa"
# print(page_verify)
# time.sleep(1)
# name_field.clear()

# 3.    checkbox
# is_selected()
# get_attribute('checked')

# <input class="form-check-input" id="exampleCheck1" type="checkbox">
# checkbox_field = driver.find_element(By.ID, "exampleCheck1")

# checkbox_field = driver.find_element(By.CLASS_NAME, "form-check-input")
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# False
# checkbox_field.click()
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# True
# print(f"checkbox_field.is_selected() is {checkbox_field.get_attribute('checked')}")
# True

# 4. radio
# Verified with is_selected()

# <input class="form-check-input" id="inlineRadio1" name="inlineRadioOptions" type="radio" value="option1">
# radio_field = driver.find_element(By.CSS_SELECTOR, "input[value='option1']")
# radio_field.click()

# radio_field_2 = driver.find_element(By.XPATH, "//input[@value='option2']")
# print(f"radido_field_2 is  Selected: {radio_field_2.is_selected()}") # False
# radio_field_2.click()
# print(f"radido_field_2 is  Selected: {radio_field_2.is_selected()}") # True
# time.sleep(1)

# 5. submit
# print("Success!" in page_verify.text)
# print(page_verify.text)

# <input class="btn btn-success" type="submit" value="Submit">

# Not working# submit_field = driver.find_element(By.CLASS_NAME, "btn btn-success")
# submit_field = driver.find_element(By.XPATH, "//input[@class='btn btn-success']")
# submit_field = driver.find_element(By.CSS_SELECTOR, "input[class*='btn-succ']")
# submit_field = driver.find_element(By.XPATH, "//input[contains(@class,'btn-succ')]")
# submit_field.click()
# <div class="alert alert-success alert-dismissible">
#                     <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#                     <strong>Success!</strong> The Form has been submitted successfully!.
#                   </div>
# page_verify = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
# page_verify = driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success']")
# page_verify = driver.find_element(By.CLASS_NAME, "alert")
# print("Success!" in page_verify.text)
# print(page_verify.text)

# 6. Date
# <input class="form-control" max="3000-12-31" min="1000-01-01" name="bday" type="date">
# date_field = driver.find_element(By.CSS_SELECTOR, "input[type='date']")
# date_field.send_keys("01/22/2020")
#
# 7. Drop Down Menu
# 1.)
# Dropdown are formed using select tag in html,
# if dropdown is not formed with select tag,
# you cannot use this Select Class methods present in python selenium

# menu_verify =  menu_field.get_attribute("value") #  Female
# make sure there is select class in html
# <select class="form-control" id="exampleFormControlSelect1">
#                         <option>Male</option>
#                         <option>Female</option>
#                       </select>

# Option with value  in html
# <option value="foo">Bar1</option>

# menu_field = driver.find_element(By.ID, "exampleFormControlSelect1")
# menu_field = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")
# menu_field = driver.find_element(By.CSS_SELECTOR, "select#exampleFormControlSelect1")
# print("this is text", type(menu_field.text)) #  str
# str_list = list(menu_field.text) # male, \n, Female \n

# menu_select = Select(menu_field)
# print(f"options {type(menu_select.options)}") # list
# print(menu_select.options[0].text) # Male

# text = 'Female'
# menu_select.select_by_visible_text(text)
# # sel.select_by_index(index) # index starts with 0 for first one
# # sel.select_by_value(val)   # need to have value attribute to work
#
# menu_verify =  menu_field.get_attribute("value") #  Female
# print(menu_verify)

# time.sleep(5)
# find_option = driver.find_element_by_xpath("//option[text()='Male']")
# find_option.click()
#
# loop_option = driver.find_elements_by_xpath("//select[contains(@id, 'Select1')]/option")
# print(len(loop_option))
# for option_item in loop_option:
#     print(option_item.text)

# 2.) Deselect
# menu_select.deselect_all()
# menu_select.deselect_by_index(index)
# menu_select.deselect_by_value(value)
# menu_select.deselect_by_visible_text(text)

# 3.)  Dynamic dropdown
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 8. ActionChains
# action.click(element_field)
# action.click_and_hold(element_field)
# action.context_click(element_field)
# action.double_click(element_field)
# action.drag_and_drop(element_field)
# action.key_down()
# action.move_to_element()

from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
url = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"
# driver.get(url)
# driver.implicitly_wait(2)
# action = ActionChains(driver)

# 8.1 right-click, then inspect
# <input type="button" id="double-click" value="Double Click Me">

# double_click_field = driver.find_element_by_id("double-click")
#   right-click with context-click
# action.context_click(double_click_field).perform()

# 8.2  double-click
# action.double_click(double_click_field).perform()
# time.sleep(2)

# 8.3 Handling Alert pop up, alert confirmation, alert  prompt
# alert = driver.switch_to.alert
# print(alert.text) # You double clicked me!!!, You got to be kidding me
# alert.accept()

# 8.4 move_to_element(element)
# driver.get('http://jqueryui.com/menu/')
# time.sleep(3)
# # define Frame
# frame = driver.find_element_by_tag_name('iframe')
# # Switch to the frame
# driver.switch_to.frame
# # define menu element
# menu_element = driver.find_element_by_id("ui-id-4")
# # define sub menu element
# sub_menu_element = driver.find_element_by_xpath("//ul/li[text()='Perch']")
# # define Action Chains
# action1 = ActionChains(driver)
# action1.move_to_element(menu_element)
# action1.perform()
# # Sleep
# time.sleep(5)
# # verify that sub menu is displayed
# print(sub_menu_element.is_displayed())

# 8.4.1 move_to_element
# Mouse move-over
# driver.get("https://www.lambdatest.com")
# action = ActionChains(driver)

# Head on the top-level menu on Lambdatest website
# <a class="nav-link" href="https://www.lambdatest.com/selenium-automation">Automation</a>
# parent_level_menu = driver.find_element_by_link_text("Automation")
# action.move_to_element(parent_level_menu).click().perform()
# parent_level_menu.click()

# code-1
# # <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="javascript:void(0)">Resources</a>
# first_level = driver.find_element(By.LINK_TEXT, "Resources")
# action.move_to_element(first_level).perform()
# # <a class="dropdown-item" href="https://www.lambdatest.com/blog">Blog</a>
# sec_level =  driver.find_element(By.LINK_TEXT, "Blog")

# The following three actions have same effect
# action.click(sec_level).perform() #  same as
# sec_level.click() # same as
# action.move_to_element(sec_level).click().perform()

# 8.5 Drag and Drop
# browser = webdriver.Chrome()
# # browse below url in google chrome.
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# # switch to iframe.
# # <iframe frameborder="0" id="iframeResult" style="height: 363.12px;"></iframe>
# browser.switch_to.frame('iframeResult')
#
# # find the drag & drop source object.
# # <div id="draggable" class="ui-draggable" style="position: relative; left: 33px; top: -6px;">请拖拽我！</div>
# source = browser.find_element_by_css_selector('#draggable')
# # find the drag & drop target object.
# # <div id="droppable" class="ui-droppable">请放置到这里！</div>
# target = browser.find_element_by_css_selector('#droppable')
# # create an ActionChains object.
# actions = ActionChains(browser)
# # connect drag & drop action source and target object.
# actions.drag_and_drop(source, target)
# # implement drag & drop action.
# actions.perform()
# time.sleep(1)
# alert = browser.switch_to.alert
# alert.accept()

# 8.6 mouse key
# 8.6.1 refresh ctrl-F5
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#
# driver.get("https://www.lambdatest.com/")
# time.sleep(2)
# print("Before refresh")
#
# ActionChains(driver) \
#     .key_down(Keys.CONTROL) \
#     .send_keys(Keys.F5) \
#     .key_up(Keys.CONTROL) \
#     .perform()
#
# print("After refresh")
# time.sleep(2)
# driver.quit()

# ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()






# 8.10
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# # find input text box
# input = browser.find_element_by_class_name('Input')
# # get input text box text.
# input_text = input.text
# # print out the text.
# # print(input_text)
# # print input text box id, location, tag_name and size
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
# time.sleep(3)
# browser.close()

# 9. Manage cookies
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# # get current web browser cookies and print.
# print(browser.get_cookies())
# # add a new cookie to web browser.
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# # delete all web browser cookies
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 10. Take screenshot
# driver = webdriver.Chrome()
# driver.get("https://www.lambdatest.com/")
#
# # 1. use relative path
# driver.save_screenshot('..\screenshot_1.png')
# # 2.
# driver.get_screenshot_as_file('screenshot_2.png')

# 11.
# 11.1
# driver.refresh()
# 11.2 open new tab
# driver.get("http://www.google.com/")
# driver.implicitly_wait(10)
# driver.execute_script("window.open('https://www.lambdatest.com','new tab')")
# time.sleep(3)
# driver.quit()

# 11.3  Execute JS code
# driver.execute_script("document.getElementsByClassName('home-cta')[0].click()")

# 11.4 extract resutls from executing JS script

# 12  Switch windows
# driver.current_window_handle
# driver.switch_to.window(driver.window_handles[0])

# driver.get('https://www.google.com')  # point to window_handles[0]
# # Open a new tab
# driver.execute_script("window.open('');")
# driver.execute_script("window.open(''), new_tab;")
# driver.switch_to.window(driver.window_handles[])
# snd_page = driver.current_window_handle

# driver.execute_script("window.open('');")
# main_page = driver.current_window_handle
# # Switch to the new tab since the focus would still be on the old window
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://lambdatest.com")
# time.sleep(1)
# # close the active tab
# driver.close()
# # Even though the tab is closed, the driver doesn't automatically switch to a differnt tab
# # Switch back to the first tab
# # driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.window(main_page)
# driver.get("https://www.yahoo.com")
# time.sleep(2)
#  # Close the only tab, will also close the browser.
# driver.close()

# 13.  Sroll on page
# window.scrollTo
# driver.get("https://www.lambdatest.com/")
# time.sleep(2)
#
# ''' Scroll to the end of the page '''
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# ''' Scroll again to the top of the page '''
# driver.execute_script("window.scrollTo(0, 0);")
#
# time.sleep(2)
# driver.quit()


# Taking screenshot
# driver = webdriver.Firefox();
#
# driver.get("https://www.facebook.com/");
#
# driver.save_screenshot('screenshot_1.png');
#
# driver.get_screenshot_as_file('screenshot_2.png');
#
# screenshot = driver.get_screenshot_as_png();
# screenshot_size = (20, 10, 480, 600);
#
# image = Image.open (StringIO.StringIO(screen));
# region = image.crop(screenshot_size);
# region.save('screenshot_3.jpg', 'JPEG', optimize=True);
#  answered Jul 22, 2019 by Abha • 27,800 points































