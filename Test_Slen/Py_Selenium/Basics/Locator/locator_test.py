from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/windows"
driver.get(url)


driver.execute_script("")

driver.execute_script("some Javascript code here")

