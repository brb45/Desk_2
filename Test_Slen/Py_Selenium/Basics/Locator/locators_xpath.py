from selenium import webdriver
import time

#--------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.unixtimestamp.com/"
driver = webdriver.Chrome()
driver.get(url)

time_loc = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/h3[2]"
time_loc1 = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/h3[2]"
time_stmp = driver.find_element_by_xpath(time_loc)
print(time_stmp.text)
# driver.quit()

# 1610498741 seconds since Jan 01 1970. (UTC)
url = "http://random-name-generator.info/"
driver.get(url)
# xpath_loc = '//*[@id="main"]/div[3]/div[2]/ol//li'
# xpath_loc = '//div[@id="main"]/div[3]/div[2]/ol//li'
xpath_loc = '//div[@id="main"]/div[3]/div[2]/ol/li[1]'
# names = driver.find_elements(By.XPATH, xpath_loc)
loc_type = By.XPATH
names = driver.find_elements(loc_type, xpath_loc)
print(type(names)) # <class 'list'>
for name in names:
    print(name.text)

#

























































































