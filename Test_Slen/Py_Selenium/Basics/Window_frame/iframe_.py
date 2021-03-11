from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

# Significance of Iframe in HTML :
# The iframe in HTML stands for Inline Frame.
# The ” iframe ” tag defines a rectangular region within the document
# in which the browser can display a separate document, including scrollbars and borders.

# iframe lets you embed an independent HTML document with its browsing context

# An inline frame is used to embed another document within the current HTML document.
# The ‘ src ‘ attribute is used to specify the URL of the document that occupies the iframe.
#
# Syntax :
#
# <iframe src="URL"></iframe>

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/iframe"
driver.get(url)

# <h3>An iFrame containing the TinyMCE WYSIWYG Editor</h3>
print(driver.find_element_by_tag_name("h3").text)

# <iframe id="mce_0_ifr"
# src="javascript:&quot;&quot;"
# frameborder="0" allowtransparency="true"
# title="Rich Text Area.
# Press ALT-F9 for menu.
# Press ALT-F10 for toolbar.
# Press ALT-0 for help" style="width: 100%; height: 100px; display: block;">
# </iframe>

frame_id = "mce_0_ifr"
driver.switch_to.frame(frame_id)

# <body id="tinymce" class="mce-content-body " onload="window.parent.tinymce.get('mce_0').fire('load');"
# contenteditable="true" spellcheck="false">
# <p>Your content goes here.</p></body>
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("body.mce-content-body ").send_keys("Test Started!")
# driver.find_element_by_css_selector("body.mce-content-body .").send_keys("QA Automation")
# selenium.common.exceptions.InvalidSelectorException

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)



time.sleep(3)
# driver.close()


























































































