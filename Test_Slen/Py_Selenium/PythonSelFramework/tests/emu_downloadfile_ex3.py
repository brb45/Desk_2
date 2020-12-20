from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","log_files\\")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "") #"application/octet-stream,application/vnd.ms-excel")
driver = webdriver.Firefox(options=options)

url = "https://www.thinkbroadband.com/download"
driver.get(url)

# <a href="http://ipv4.download.thinkbroadband.com/5MB.zip">
# <img src="../../../assets/images/download-files/iconDownload-5MB.png" alt="">
# </a>

download_img = driver.find_element_by_xpath("//img[contains(@src, '5MB.png')]")
# download_img = driver.find_element_by_css_selector("img[src='../../../assets/images/download-files/iconDownload-5MB.png']")
# download_img = driver.find_element_by_css_selector("img[src*='iconDownload-5MB.png']")

download_img.click()

# alert = driver.switch_to.alert
# print(alert.text)
# alert.dismiss()


time.sleep(10)
driver.close()



