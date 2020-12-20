from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

class RunChromeTestWindows():
    def test(self):
        driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)
        driver = webdriver.Chrome()
        #driver.get("http://www.letskodeit.com")
        driver.get("http://www.google.com")
        search_box = driver.find_element_by_name("q")
        time.sleep(5)

        # type in query
        search_box.send_keys("seleniumhq" + Keys.RETURN)
        # search_box.send_keys("seleniumhq")
        time.sleep(4)
        print(driver.title)

        # driver.quit()



chromeTest = RunChromeTestWindows()
chromeTest.test()




