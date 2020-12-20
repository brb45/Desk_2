from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

# https://rahulshettyacademy.com/seleniumPractise/#/
# //div[@class='product-action']/button/parent::div/parent::div
#
#explicit wait:
#
# Not global, only apply for target execution

# alert = driver.switch_to.alert
# alert.accept()
# Java, javascript alert
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
# url = "https://rahulshettyacademy.com/AutomationPractice/"

# driver.implicitly_wait(1000)
url ="https://rahulshettyacademy.com/seleniumPractise/"

driver.get(url)
# driver.maximize_window()

item_select_list = []
veg_list = []
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
# //div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons_to_click:
    item_select_list.append((button.find_element_by_xpath("parent::div/parent::div/h4").text))
    button.click()
    time.sleep(1)
    # break
# time.sleep(29)
shopping_cart = driver.find_element_by_css_selector("img[alt='Cart']")
shopping_cart.click()

checkout = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
checkout.click()

explicit_wait = WebDriverWait(driver, 5)
explicit_wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veg = driver.find_elements_by_css_selector("p.product-name")
for item in veg:
    veg_list.append(item.text)

originalAmount = driver.find_element_by_css_selector(".discountAmt").text

promo_code = driver.find_element_by_class_name("promoCode")
promo_code.send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()

explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

#
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountAmount) < float(originalAmount)

# time.sleep(10)
print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum += int(amount.text)
total = int(driver.find_element_by_class_name("totAmt").text)

print(f"{total} == {sum}")
# assert total == amounts

# Test case
assert  item_select_list == veg_list
print(f"item_select_list is {item_select_list}")
print(f"veg_list is         {veg_list}")



time.sleep(3)
driver.close()


























































































