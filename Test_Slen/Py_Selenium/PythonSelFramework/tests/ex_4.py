# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = webdriver.Chrome()
# driver.get('http://www.w3schools.com/')
# target = driver.find_element_by_link_text('BROWSE TEMPLATES')
# actions = ActionChains(driver)
# actions.move_to_element(target)
# actions.click(target)
#
# # target.click()
# time.sleep(5)
# driver.close()

# import webdriver class.
from selenium import webdriver
# import ActionChains class.
from selenium.webdriver import ActionChains
import time
# create google chrome web browser.
browser = webdriver.Chrome()
# browse below url in google chrome.
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# switch to iframe.
browser.switch_to.frame('iframeResult')
# find the drag & drop source object.
source = browser.find_element_by_css_selector('#draggable')
# find the drag & drop target object.
target = browser.find_element_by_css_selector('#droppable')
# create an ActionChains object.
actions = ActionChains(browser)
# connect drag & drop action source and target object.
actions.drag_and_drop(source, target)
# implement drag & drop action.
actions.perform()#执行动作
time.sleep(1)
alert = browser.switch_to.alert
alert.accept()