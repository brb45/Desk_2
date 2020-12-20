from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from log_locator_1 import WikipediaHomepage, WikipediaArticle
from selenium.webdriver.common.by import By
import os, time


class WikipediaHomepage():
    random_link = (By.CSS_SELECTOR, '#n-randompage')

class WikipediaArticle():
    first_heading = (By.CSS_SELECTOR, '.firstHeading')
    page_info = (By.LINK_TEXT, 'Page information')
    search_box = (By.NAME, 'search')

    # XPath
    Logo = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/a')


class RunChromeTestWindows():
    def test(self):
        # driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)
        driver = webdriver.Chrome()
        driver.get("https://en.wikipedia.org")

        # random_link = (By.CSS_SELECTOR, '#n-randompage')
        # < li id = "n-randompage" >
        #   < a href = "/wiki/Special:Random"  title = "Load a random article [alt-shift-x]"
        # accesskey = "x" > Random article < / a >
        #   < / li >
        random_link = driver.find_element(*WikipediaHomepage.random_link) # use CSS_SELECTOR by ID
        random_link.click()
        time.sleep(3)

        # print random article's title from above
        # < h1 id = "firstHeading" class ="firstHeading" lang="en" > Main Page < / h1 >
        # first_heading = (By.CSS_SELECTOR, '.firstHeading')
        first_heading = driver.find_element(*WikipediaArticle.first_heading)
        print(f"first_heading.text is {first_heading.text}")
        time.sleep(2)

        # # click on page information
        # page_info = driver.find_element(*WikipediaArticle.page_info)
        # page_info.click()
        # time.sleep(3)
        #
        # # input in searchbox
        # search_box = driver.find_element(*WikipediaArticle.search_box)
        # search_box.send_keys("Selenium (Software)" + Keys.RETURN)
        # time.sleep(3)
        #
        # # Xpath
        # Logo = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/a')
        # logo = driver.find_element(*WikipediaArticle.Logo)
        # logo.click()
        time.sleep(3)
        
        # driver.quit()





chromeTest = RunChromeTestWindows()
chromeTest.test()


 


 