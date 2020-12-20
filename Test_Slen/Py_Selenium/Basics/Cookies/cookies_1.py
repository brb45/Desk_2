from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://login.yahoo.com/?.intl=us&.lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com%2Fd&add=1"
driver.get(url)
time.sleep(1)
print(driver.title)
print(driver.current_url)
driver.maximize_window()

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

next_button = driver.find_element_by_css_selector("button[name='verifyPassword']")
print(next_button.get_attribute('innerHTML'))
# Next
print(next_button.get_attribute('outerHTML'))
# <button type="submit" id="login-signin" class="pure-button puree-button-primary puree-spinner-button challenge-button" name="verifyPassword" value="Next" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:password-challenge-next">
#                     Next
#             </button>
with open("page_source.txt", "w", encoding='utf-8') as fout:
    fout.write(driver.page_source)
# print(type(driver.page_source)) # string
next_button.click()
time.sleep(200)

cookies = driver.get_cookies()
print(cookies) # A list of cookies of type dict

with open("cookies_file.txt", "w") as fout:
    for dic in cookies:
        fout.write(str(dic)+'\n')
driver.close()


url = "https://mail.yahoo.com/"
driver = webdriver.Chrome()
driver.get(url)

# load_cookie(driver)
for c in cookies:
    driver.add_cookie(c)
time.sleep(2)
driver.refresh()
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# driver.close()


















































































