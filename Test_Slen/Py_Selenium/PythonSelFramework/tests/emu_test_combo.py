from selenium import webdriver
import selenium
from selenium.webdriver.support.select import Select
import time
# driver = webdriver.Chrome()
# url = "https://rahulshettyacademy.com/angularpractice/"
# # url = "https://www.lambdatest.com/"
# driver.get(url)
# # time.sleep(5)
# # driver.close()
# # driver.maximize_window()
#
# from selenium.webdriver.common.by import By
#
# # # <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# # # <input class="form-control ng-untouched ng-dirty ng-valid" minlength="2" name="name" required="" type="text">
# # name_text_field = driver.find_element(By.NAME, "name")
# #
# # print(selenium.__version__)
# # # element.get_attribute('innerHTML')
#
#
#
#
# #
# # # 1. use relative path
# # driver.save_screenshot('..\screenshot_1.png')
# # # 2.
# driver.get_screenshot_as_file('log_files\screenshot_ex.png')
# # driver.get_screenshot_as_png()
#
# time.sleep(5)
# driver.close()

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support      import expected_conditions as EC
driver = webdriver.Chrome()
# driver.implicitly_wait(2)

url = "https://www.fortinet.com/"
driver.get(url)
action_item = ActionChains(driver)
support_field = driver.find_element_by_link_text("Support")
action_item.move_to_element(support_field).perform()
explicit_wait  = WebDriverWait(driver, 2)
explicit_wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Product Support")))


click_field = driver.find_element_by_link_text("Product Support")
# action_item.click(click_field).perform()
click_field.click()
driver.get_screenshot_as_file("log_files\productSupport.png")
print(driver.title)
# action_item.move_to_element(support_field).click(click_field).perform()
# <a class="button--transparent" target="_blank" href="/content/dam/fortinet/assets/brochures/FortiCare-Services.pdf">
#                     Download FortiCare Brochure to learn more
#                 </a>
# download_button = driver.find_element(By.CSS_SELECTOR, "a[class*='tran']")
download_button = driver.find_element(By.CSS_SELECTOR, "a.button--transparent")
download_button.click()

driver.switch_to.window(driver.window_handles[1])
# <embed id="plugin" type="application/x-google-chrome-pdf" src="https://www.fortinet.com/content/dam/fortinet/assets/brochures/FortiCare-Services.pdf" stream-url="chrome-extension://mhjfbmdgcfjbbpaeojofohoefgiehjai/93889027-4cdd-4145-89ec-2a6a325a7996" headers="Accept-Ranges: bytes
# Content-Encoding: gzip
# Content-Type: application/pdf
# Date: Sat, 14 Mar 2020 00:37:17 GMT
# ETag: &quot;3de43-58a1f47a26e80-gzip&quot;
# Last-Modified: Thu, 30 May 2019 18:43:54 GMT
# Server: Apache
# Vary: Accept-Encoding,User-Agent
# X-Content-Type-Options: nosniff
# X-Dispatcher: dispatcher2uswest1
# X-Frame-Options: SAMEORIGIN
# X-Vhost: publish
# content-length: 68730
# " background-color="0xFF525659" top-toolbar-height="56" javascript="allow" full-frame="">
# <input id="input" part="input" aria-invalid="false" tabindex="0" aria-label="Page number">
#
time.sleep(1)
print(driver.current_url)
# <div id="aligner"><span id="title" title="FortiCare-Services.pdf"><span>FortiCare-Services.pdf</span></span><div id="pageselector-container"><viewer-page-selector id="pageselector" class="" style="--page-length-digits:1;"></viewer-page-selector></div><div id="buttons" class=""><dom-if style="display: none;"><template is="dom-if"></template></dom-if><cr-icon-button id="rotate-right" iron-icon="pdf:rotate-right" aria-disabled="false" role="button" tabindex="0" title="Rotate clockwise" aria-label="Rotate clockwise"></cr-icon-button><cr-icon-button id="download" iron-icon="cr:file-download" aria-disabled="false" role="button" tabindex="0" title="Download" aria-label="Download"></cr-icon-button><cr-icon-button id="print" iron-icon="cr:print" aria-disabled="false" role="button" tabindex="0" aria-label="Print" title="Print"></cr-icon-button><viewer-toolbar-dropdown id="bookmarks" selected="" metrics-id="bookmarks" open-icon="pdf:bookmark" closed-icon="pdf:bookmark-border" hidden=""><dom-repeat style="display: none;"><template is="dom-repeat"></template></dom-repeat></viewer-toolbar-dropdown></div></div>
# time.sleep(2)
# move_bar = driver.find_element(By.ID, "aligner")
# action_item.move_to_element(move_bar).perform()
# print_field = driver.find_element(By.CSS_SELECTOR, "#print")
# action_item.click(print_field)
# time.sleep(1)
# driver.get_screenshot_as_file("log_files\print.png")
# driver.close()
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.close()

# Deal with file upload and download







































