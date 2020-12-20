from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .log_locator_1 import WikipediaHomepage, WikipediaArticle
import os, time
from .log_auth_2 import LoginPage, CreateAccountPage

class RunChromeTestWindows():
    def test(self):
        # driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000") # a login page

        # Log-in success
        username = driver.find_element(*LoginPage.username_field)
        password = driver.find_element(*LoginPage.password_field)
        submit = driver.find_element(*LoginPage.submit_btn)
        username.send_keys("jsun")
        password.send_keys("1234")
        submit.click()
        time.sleep(3)

        welcome_message = driver.find_element(*LoginPage.message)
        print(welcome_message.text)
        
        driver.quit()





chromeTest = RunChromeTestWindows()
chromeTest.test()


 


 