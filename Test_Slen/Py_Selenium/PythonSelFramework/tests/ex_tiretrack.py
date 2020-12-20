
from selenium import webdriver
import time

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by    import By
from selenium.webdriver.common.keys  import Keys


from selenium.webdriver.support        import expected_conditions
from selenium.webdriver.support.wait   import WebDriverWait
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument('--disable-notifications')
options.add_argument('--incognito')
options.add_argument("download.default_directory=")
# driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome()
# driver.implicitly_wait(2)

url = "https://www.tirerack.com/content/tirerack/desktop/en/homepage.html"
driver.get(url)

# is_displayed()
# Whether the element is visible to a user.
#
# is_enabled()
# Returns whether the element is enabled.
#
# Refer transferfund_scenario.py file
#
# is_selected()

# explicit_wait = WebDriverWait(driver, 10)
# explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
# time.sleep(10)
# print(driver.find_element_by_css_selector("span.promoInfo").text)
site_name=driver.find_element_by_css_selector("img[alt='TireRack.com']")

explicit_wait = WebDriverWait(driver, 4)
explicit_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img[alt='TireRack.com']" )))
print(site_name.get_attribute('alt'))

# <a href="/content/tirerack/desktop/en/tires.html" onclick="toggleMainNav('1');linkTracking({linkName: 'tr: nav: tires'},'','o'); return false;">Tires</a>
# <a href="/modalPopups/changeSearchLayer.jsp?shoppingFor=tires" onclick="openInfoBox(this.href,'','default','default','none'); return false;">By Vehicle</a>
Tires = driver.find_element_by_link_text("Tires")
Tires.click()
# visibility_of_element_located vs presence_of_element_located
explicit_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'By Vehicle')))
by_vehicle = driver.find_element_by_css_selector("a[href*='shoppingFor=tires']")
print(by_vehicle.get_attribute('text'))

actions = ActionChains(driver)

# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(3)
driver.close()









































