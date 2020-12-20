from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time

download_dir = "log_files\\"
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "log_files\\",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')


chrome_options.add_argument("download.default_directory=log_files\\")

# options.add_argument("--start-maximized")
# prefs = {"profile.default_content_settings.popups": 0,
#              "download.default_directory":
#                         r"C:\Users\user_dir\Desktop\\",#IMPORTANT - ENDING SLASH V IMPORTANT
#              "directory_upgrade": True}
# options.add_experimental_option("prefs", prefs)
# browser=webdriver.Chrome(<chromdriver.exe path>, options=options)


# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(options=chrome_options)

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


time.sleep(100)
driver.close()



