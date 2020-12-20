from selenium import webdriver
import time
import pickle

def save_cookie(driver):
    with open("cookie_yahoo", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver):
     with open("cookie_yahoo", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             print(cookie, "\n")
             driver.add_cookie(cookie)

driver = webdriver.Chrome()
# url = "https://login.yahoo.com/?.intl=us&.lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com%2Fd&add=1"
# driver.get(url)
# time.sleep(1)

url = "https://mail.yahoo.com/"
driver.get(url)
load_cookie(driver)
time.sleep(2)
driver.refresh()
driver.maximize_window()
print(driver.title)
print(driver.current_url)


# import getpass
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(
#     "user-data-dir=C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # this is the directory for the cookies
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get(url)























































































