# HTML locators:
# CSS selector, Name, Link text, Tag name,

# CSS seletor:
# ID ("#n-randompage")
# Class('.fistHeading')
# Attribute values(tag[attribute=value])

# Name locators
# Not unique

# Link Text: locate hyperlinks only <a>
# Not unique

# HTML Tag name:
# img, a, div, ...

from selenium.webdriver.common.by import By

class WikipediaHomepage():
    random_link = (By.CSS_SELECTOR, '#n-randompage')

class WikipediaArticle():
    first_heading = (By.CSS_SELECTOR, '.firstHeading')
    page_info = (By.LINK_TEXT, 'Page information')
    search_box = (By.NAME, 'search')

    # XPath
    Logo = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/a')






