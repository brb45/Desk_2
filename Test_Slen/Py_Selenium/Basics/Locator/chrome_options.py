from selenium import webdriver
import time


def driver(browser):
    if browser == 'firefox':
        return webdriver.Firefox()
    if browser == 'chrome':
        return webdriver.Chrome('chromedriver.exe')
    if browser == 'opera':
        # TODO: Opera implementation is quite buggy annoyingly. It won't close at the moment
        # Need to investigate.
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Program Files\\Opera\\launcher.exe"
        return webdriver.Opera(executable_path='operadriver.exe', opera_options=options)
    if browser == 'ie':
        return webdriver.Ie()
    if browser == 'edge':
        # TODO: check for Windows < 8.1?
        return webdriver.Edge()
    if browser == 'phantom':
        return webdriver.PhantomJS()
    raise XVEx("{} is not supported on {}".format(browser, self._device.os_name()))

def chrome(headless=False):
    # support to get response status and headers
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    opt = webdriver.ChromeOptions()
    if headless:
        opt.add_argument("--headless")
    opt.add_argument("--disable-xss-auditor")
    opt.add_argument("--disable-web-security")
    opt.add_argument("--allow-running-insecure-content")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-setuid-sandbox")
    opt.add_argument("--disable-webgl")
    opt.add_argument("--disable-popup-blocking")
    # prefs = {"profile.managed_default_content_settings.images": 2,
    #          'notifications': 2,
    #          }
    # opt.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=opt,desired_capabilities=d)
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(20)
    return browser

def headless(self, path: str, proxy: str = "") -> None:
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1500,1200")
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("disable-gpu")
        options.add_argument("log-level=3")
        options.add_argument(f"user-agent={userAgent}")

        if proxy != "":
            self.proxy = True
            options.add_argument("proxy-server={}".format(proxy))

        self.driver = webdriver.Chrome(path, chrome_options=options)
        self.set_config()
        self._headless = True

def load_driver(settings):
    """
    Load the Selenium driver depending on the browser
    (Edge and Safari are not running yet)
    """
    driver = None
    if settings['browser'] == 'firefox':
        firefox_profile = webdriver.FirefoxProfile(settings['browser_path'])
        driver = webdriver.Firefox(firefox_profile)
    elif settings['browser'] == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-data-dir=' +
                                    settings['browser_path'])
        driver = webdriver.Chrome(options=chrome_options)
    elif settings['browser'] == 'safari':
        pass
    elif settings['browser'] == 'edge':
        pass

    return driver

def test_operadriver_manager_with_selenium():
    driver_path = OperaDriverManager().install()
    options = webdriver.ChromeOptions()
    options.add_argument('allow-elevated-browser')

    if get_os_type() in ["win64", "win32"]:
        paths = [f for f in glob.glob(f"C:/Users/{os.getlogin()}/AppData/" \
                                      "Local/Programs/Opera/**",
                                      recursive=True)]
        for path in paths:
            if os.path.isfile(path) and path.endswith("opera.exe"):
                options.binary_location = path
    elif ((get_os_type() in ["linux64", "linux32"]) and not
          os.path.exists('/usr/bin/opera')):
        options.binary_location = "/usr/bin/opera"
    elif get_os_type() in "mac64":
        options.binary_location = "/Applications/Opera.app/Contents/MacOS/Opera"

    ff = webdriver.Opera(executable_path=driver_path, options=options)
    ff.get("http://automation-remarks.com")
    ff.quit()

def driver1():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-gpu")
    options.add_argument("headless")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument("no-sandbox")

    d = DesiredCapabilities.CHROME
    d["loggingPrefs"] = {"browser": "ALL"}

    driver = webdriver.Chrome(options=options, desired_capabilities=d)
    driver.implicitly_wait(30)

    yield driver
    driver.quit()

def _open_webdriver(self):  # 该函数同时作为重启 webdriver 功能使用
        try:
            self.spider_closed()
        except:
            pass
        from selenium import webdriver
        option = webdriver.ChromeOptions()
        extset = ['enable-automation', 'ignore-certificate-errors']
        ignimg = "profile.managed_default_content_settings.images"
        mobile = {'deviceName': 'Galaxy S5'}
        option.add_argument("--disable-infobars")  # 旧版本关闭“chrome正受到自动测试软件的控制”信息
        option.add_experimental_option("excludeSwitches", extset)  # 新版本关闭“chrome正受到自动测试软件的控制”信息
        option.add_experimental_option("useAutomationExtension", False)  # 新版本关闭“请停用以开发者模式运行的扩展程序”信息
        # option.add_experimental_option('mobileEmulation', mobile)     # 是否使用手机模式打开浏览器
        # option.add_experimental_option("prefs", {ignore_image: 2})    # 开启浏览器时不加载图片(headless模式该配置无效)
        # option.add_argument('--start-maximized')                      # 开启浏览器时是否最大化(headless模式该配置无效)
        # option.add_argument('--headless')                             # 无界面打开浏览器
        # option.add_argument('--window-size=1920,1080')                # 无界面打开浏览器时候只能用这种方式实现最大化
        # option.add_argument('--disable-gpu')                          # 禁用 gpu 硬件加速
        # option.add_argument("--auto-open-devtools-for-tabs")          # 开启浏览器时候是否打开开发者工具(F12)
        # option.add_argument("--user-agent=Mozilla/5.0 HELL")          # 修改 UA 信息
        # option.add_argument('--proxy-server=http://127.0.0.1:8888')   # 增加代理
        self.webdriver = webdriver.Chrome(chrome_options=option)


def __init__(self, username, password):
    self.driver = None

    self.last_access = time.time()

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    options.binary_location = "/usr/lib/chromium-browser/chromium-browser"
    self.driver = webdriver.Chrome(chrome_options=options)

    self.driver.set_window_size(1920, 1080)
    self.driver.get(CardSender.url)
    usr_box = self.driver.find_element_by_id('email')
    usr_box.send_keys(username)
    pass_box = self.driver.find_element_by_id('password')
    pass_box.send_keys('{}\n'.format(password))








    #___________________________________________________
url = ""
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

print(driver.title)
print(driver.current_url)
# assert "ProtoCommerce" == driver.title
# assert url == driver.current_url

loc_name = 'name'
name = driver.find_element_by_name(loc_name)
name.send_keys("Tester")
print("type is ", type(name))
# type is  <class 'selenium.webdriver.remote.webelement.WebElement'>
print("name is ",  name)
# name is  <selenium.webdriver.remote.webelement.WebElement
# (session="94fa27fad67123e5ae7c85c929ef9b4e", element="02ed17af-de1a-416d-913c-b10ada98077b")>

email = driver.find_element_by_name("email")
email.send_keys('ssqa@litepoint.com')
print("email is ", email)
# email is  <selenium.webdriver.remote.webelement.WebElement
# (session="8857d3be73a46388386244b14b30e8e7", element="fd4c8122-59a0-4757-a197-f74c6907bfb5")>
id = driver.find_element_by_id("exampleCheck1")
id.click()

#
# #@@ 3. class name: not recommended since hard to find unique one.
# # find_classname = driver.find_element_by_class_name()
#
# #@@ 4. css, need to be unique
# # tagname[attribute="value"] --> Tagname optional
# # <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">

# # input[name='name']

find_css = driver.find_element_by_css_selector("input[name='name']")
find_css.clear()
find_css.send_keys("ssqa_test")
#
# #@@ 5. Xpath
# # //tagname[@attribute=value] ==> tagname optional
# # //input[@type='submit']
# # $x("//input[@type='submit']")
# # [input.btn.btn-success]
# # 0: input.btn.btn-success
# # length: 1
# # __proto__: Array(0)

# xpath1 = "//input[@type='submit']"
xpath  = "//input[@class='btn btn-success']"
find_xpath = driver.find_element_by_xpath(xpath)
find_xpath.click()
# ## getattribute()
# find_xpath.get_attribute(attribute_name)
#
# #@@ 6.
# <div class="alert alert-success alert-dismissible">
#                     <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#                     <strong>Success!</strong> The Form has been submitted successfully!.
# </div>

# import time
# time.sleep(3)
# NOT WORKING
# alert = driver.find_element_by_class_name("alert alert-success alert-dismissible")
# alert_text = alert.text
# print(alert_text)

css_selector = "div[class='alert alert-success alert-dismissible']"
alert_message = driver.find_element_by_css_selector(css_selector)
text = alert_message.text
print(text)
print("-------------------------------")
#
# if "success!" in text:
#     print(True)
# if "Success!" in text:
#     print("Success!")
# assert "uccesws" in text
# #___________________
#
#
# customize css_selector tagname[attribute*='value']
# <div class="alert alert-success alert-dismissible">
css_select = "div[class*='alert-success']"
show_text1  = driver.find_element_by_css_selector(css_select)
print(show_text1.text)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# #
# # customize Xpath
# # //tagname[contains(@attribute, 'value')]
xpath_custom = "//*[contains(@class, 'alert-success')]"
show_text2 = driver.find_element_by_xpath(xpath_custom)
print(show_text2.text)
print("**************************")
#



# NOT working
xpath_1 = "//*[contains(text(),'successful')]"
# show_text3 = driver.find_element_by_xpath(xpath_1)
# print(show_text3.text)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(driver.execute_script("return navigator.userAgent"))
time.sleep(5)
driver.close()
#
# ## Generate css from ID
# # tagname#ID
#
# ## xpath text()
# # "//tagname[text()= text_string]"
# driver.find_element_by_xpath("//a[text()='Cancel']").click()
#
# ##
