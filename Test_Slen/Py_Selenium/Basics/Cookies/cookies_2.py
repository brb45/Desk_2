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
url = "https://login.yahoo.com/?.intl=us&.lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com%2Fd&add=1"
driver.get(url)
# time.sleep(1)
# print(driver.title)
print(driver.current_url)
# driver.maximize_window()

user = "pice.bong@yahoo.com"
passwd = "aA12345!"
# <input class="phone-no " type="text" name="username" id="login-username" tabindex="1"
# value="" autocomplete="username" autocapitalize="none" autocorrect="off" autofocus="true" placeholder=" ">
driver.find_element_by_css_selector("#login-username").send_keys(user)
time.sleep(1)
# <input id="login-signin" type="submit" name="signin" class="pure-button puree-button-primary challenge-button"
# value="Next" tabindex="6" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:login-landing-next"
# aria-hidden="false">
driver.find_element_by_xpath("//input[@name='signin']").click()
time.sleep(1)

# <input type="password" id="login-passwd" class="password" name="password"
# placeholder=" " autofocus="" autocomplete="current-password"
# data-rapid-tracking="true" data-ylk="elm:input;elmt:focus;slk:passwd;mKey:password-challenge-focus-passwd">
driver.find_element_by_css_selector("#login-passwd").send_keys(passwd)

# <button type="submit" id="login-signin"
# class="pure-button puree-button-primary puree-spinner-button challenge-button"
# name="verifyPassword" value="Next" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:password-challenge-next">
#                     Next
#             </button>
driver.find_element_by_css_selector("button[name='verifyPassword']").click()
time.sleep(1)

save_cookie(driver)
url = driver.current_url
print(url)
driver.quit()
print("------------------------------------")
driver = webdriver.Chrome()
# time.sleep(5)
# url = "https://mail.yahoo.com/"
driver.get(url)
load_cookie(driver)
time.sleep(2)
driver.refresh()
driver.maximize_window()
print(driver.title)
print(driver.current_url)

"""
Suppose we have to test for the following scenario:

1. Go to login page and login to the application
2. Close the browser
3. Open the browser and go to the login page - the user should not see the login form and should be already logged in.

On the first login, cookies are stored in the browser. In WebDriver, when the browser window is closed, 
all session data and cookies are deleted, so the testing of the above scenario becomes impossible.

Luckily, WebDriver has functionality to read the cookies from the browser before closing it and 
then restore the cookies in the new browser window.
"""

# import getpass
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(
#     "user-data-dir=C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # this is the directory for the cookies
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get(url)























































































