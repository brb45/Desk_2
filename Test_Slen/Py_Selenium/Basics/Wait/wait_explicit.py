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

explicit_wait = WebDriverWait(driver, 5)
explicit_wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

promo_code = driver.find_element_by_class_name("promoCode")
promo_code.send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()


# EC.presence_of_all_elements_located
# EC.presence_of_element_located

# EC.text_to_be_present_in_element
# EC.text_to_be_present_in_element_value
# EC.title_contains
# EC.title_is
# EC.url_contains

# EC.visibility_of_any_elements_located
# EC.visibility_of_any_elements_located
# EC.visibility_of_all_elements_located

# EC.alert_is_present
# EC.element_to_be_clickable
# EC.element_to_be_selected
# EC.frame_to_be_available_and_switch_to_it
# EC.new_window_is_opened



explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
# time.sleep(10)
print(driver.find_element_by_css_selector("span.promoInfo").text)

time.sleep(3)
# driver.close()


# Let take example: We have driver with below values & assume compose element will not be visible for 50 seconds
# Implicit wait :15 second
# Explicit wait : 5 Second.
#
# WebDriverWait wait = new WebDriverWait(drv,5);
#
# wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(“//div[contains(text(),’COMPOSE’)]”)));
#
# So what do you thing ,For how much time driver will wait for element ?
# Answer : 15 second :) People will say its wrong answer
# Why?
#
# Go to selenium code for Expected conditions class
# https://github.com/SeleniumHQ/selenium/blob/master/java/client/src/org/openqa/selenium/support/ui/ExpectedConditions.java
#
# Its using driver.findElement(by) which will wait for 15 second as specified in implicit wait.
#
# Whevener you are using explicit wait ,use below example
#
# //Set implicit wait to ZERO
# driver.manage().timeouts().implicitlyWait(0, TimeUnit.SECONDS);
#
# T returnValue = new WebDriverWait(driver, timeOutInSeconds).until(expectedCondition);
#
# //After running code above code set implicit wait to desired value
# driver.manage().timeouts().implicitlyWait(15,TimeUnit.SECONDS);

Condition for Explicit wait in selenium webdriver
























































































