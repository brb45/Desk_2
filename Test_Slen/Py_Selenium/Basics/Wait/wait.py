from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
#implicit wait:
# driver.implicitly_wait(n)
# Global wait for each action;
# maximum wait is n seconds
# if wait is less than n seconds, following actions resume

# alert = driver.switch_to.alert
# alert.accept()
# Java, javascript alert
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
# url = "https://rahulshettyacademy.com/AutomationPractice/"

driver.implicitly_wait(1000)
url ="https://rahulshettyacademy.com/seleniumPractise/"

driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()

# @@ 5. wait
css_select = "input[class='search-keyword']"
# or
# css_select = "input.search-keyword"
driver.find_element_by_css_selector(css_select).send_keys("ber")
time.sleep(3)
# //div[@class='products']/div
xpath_sel = "//div[@class='products']/div"
products = driver.find_elements_by_xpath(xpath_sel)

# assert len(products) == 3
print(len(products))


buttons_to_click = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons_to_click:
    button.click()
    # break
# time.sleep(29)
shopping_cart = driver.find_element_by_css_selector("img[alt='Cart']")
shopping_cart.click()

checkout = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
checkout.click()

promo_code = driver.find_element_by_class_name("promoCode")
promo_code.send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()

print(driver.find_element_by_css_selector("span.promoInfo").text)
time.sleep(3)
driver.close()


























































































