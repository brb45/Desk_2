from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# for easy future changes and code maintainbility i have added all the locators and parameters like username/password at the top of the test
driver = webdriver.Chrome()
CONTINUE_BUTTON = (By.XPATH,'//*[@id="cms-search-panel-container"]/div/div/div/form/div[3]/div/button')
FLIGHT_CLASS_DROPDOWN = (By.ID,'serviceclass')
FLIGHT_CLASS_NAME = 'BUSINESS'
URL = 'https://www.airnewzealand.co.nz/home'

class AirNZ_flight_class:

    def verify_flight_class_dropdown_value(self):
        driver.maximize_window()
        driver.get(URL)
        # wait for the continue button to appear
        continue_button = WebDriverWait(driver,10).until(EC.presence_of_element_located(CONTINUE_BUTTON))
        continue_button.click()
        # wait for the fligh class dropdown to appear
        flight_class_dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located(FLIGHT_CLASS_DROPDOWN))
        #select the drop down using the Select class imported from from selenium.webdriver.support.select
        select = Select(flight_class_dropdown)
        try:
            # select an option from the drop down based on a value, i did not go for a index in case the index changes due to addition or removal of entries
            select.select_by_value(FLIGHT_CLASS_NAME)
        except(NoSuchElementException,TimeoutException) as e:
            # fail the Test if the element can not be found or timeout occurs
            print('Test failed, the flight class drop down could not be found ')
        finally:
            driver.quit()

test = AirNZ_flight_class()
test.verify_flight_class_dropdown_value()