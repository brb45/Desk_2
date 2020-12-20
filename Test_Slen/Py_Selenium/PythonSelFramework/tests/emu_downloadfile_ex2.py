
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from selenium import webdriver
# Using Chrome to access web
options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=C:/Test") # Set the download Path
driver = webdriver.Chrome(options=options)
# Open the website
try:
    driver.get('xxxx') # Your Website Address
    password_box = driver.find_element_by_name('password')
    password_box.send_keys('xxxx') #Password
    download_button = driver.find_element_by_class_name('link_w_pass')
    download_button.click()
    driver.quit()
except:
    driver.quit()
    print("Faulty URL")

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="<path_to_chrome_driver>")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file

download_dir = "log_files\\"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

# get request to target the site selenium is active on
driver.get("https://www.thinkbroadband.com/download")

# initialize an object to the location on the html page and click on it to download
search_input = driver.find_element_by_css_selector('#main-col > div > div > div:nth-child(8) > p:nth-child(1) > a > img')
search_input.click()