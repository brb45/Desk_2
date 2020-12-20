from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time, selenium

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
# driver.get(url)
# driver.maximize_window()
# driver.close()

# selenium.__version__
# ???


#
#


# name_text_field.is_selected()
# name_text_field.screenshot("filename")
# name_text_field.screenshot_as_png
# name_text_field.submit()

# sel.deselect_all()
# sel.deselect_by_index(index)
# sel.deselect_by_value(value)
# sel.deselect_by_visible_text(text)

# sel.select_by_visible_text(text)
# sel.select_by_index(index)
# sel.select_by_value(val)

# 0. is_displayed()
# is_displayed() --> Element is visible on webpage
# <label>Name</label>
# name_field = driver.find_element_by_xpath("//label[text()='Name']")
# print(f"name_field is {name_field.text}")
# # name_field is Name
# try:
#     print(f"name_field displayed: {name_field.is_displayed()}")
#     # name_field displayed: True
# except:
#     print(f"name_field is NOT displayed")
# driver.close()

tmp_str = ""
# 1. click(link)
# <a class="nav-link" href="/angularpractice/shop">Shop</a>
#  https://rahulshettyacademy.com/angularpractice

# driver.find_element_by_tag_name(tmp_str)
# driver.find_elements_by_tag_name(tmp_str)
#
# driver.find_element_by_id(tmp_str)
# driver.find_element_by_class_name(tmp_str)
# driver.find_element_by_name(tmp_str)
# driver.find_element_by_link_text(tmp_str)
# driver.find_element_by_partial_link_text(tmp_str)

# driver.find_element_by_xpath(tmp_str)
# driver.find_element_by_css_selector(tmp_str)

# driver.find_element(by, value)

# selenium.common.exceptions.InvalidSelectorException: Message:

driver.set_page_load_timeout(60)
driver.current_url
driver.current_window_handle
driver.delete_all_cookies()
driver.delete_cookies(tmp_str)
driver.forward()
driver.back()
driver.execute_script()
driver.get_cookies()
driver.get_network_conditions()

driver.implicitly_wait(time_to_wait  = 1)
driver.fullscreen_window()
driver.get_log()
driver.launch_app(id)
driver.maximize_window()
driver.minimize_window()
driver.quit()
driver.refresh()

driver.session_id
driver.switch_to.alert
driver.switch_to.window(window_name)
driver.switch_to.default_content()

driver.switch_to.frame(frame_ref)
driver.switch_to.parent_frame()
driver.switch_to.

driver.get_screenshot_as_png()
driver.get_screenshot_as_file()
driver.save_screenshot(file_name)
driver.get_screenshot_as_file("yahoo_finance.png")

driver.page_source
with open('html_element.html', 'w') as f:
    f.write(name_text_field.get_attribute('outerHTML'))

with  open("html_src_code.html", "w", encoding="utf-8") as fout:
    fout.write(driver.page_source)







