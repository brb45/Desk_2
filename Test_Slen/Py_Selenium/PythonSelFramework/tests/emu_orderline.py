from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. implicit wait

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(url)
driver.implicitly_wait(14)

# 1.
# <input type="search" placeholder="Search for Vegetables and Fruits" class="search-keyword">
# driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
# driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
# driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")

# 2.
# <button class="" type="button">ADD TO CART</button>
# "//button[text()='ADD TO CART']"
# //div[@class='product']/div/button
product_list = driver.find_elements_by_xpath("//div[@class='products']/div")
# assert len(product_list) == 3

driver.find_element_by_xpath("//div[@class='product-action']/button").click()
# for button in add_to_cart_buttons:
#     button.click()
#     break
#     time.sleep(2)

# 3.
# <img class=" " src="https://res.cloudinary.com/sivadass/image/upload/v1493548928/icons/bag.png" alt="Cart" xpath="1">
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# <button type="button" class=" " xpath="1">PROCEED TO CHECKOUT</button>
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# <input type="text" class="promoCode" placeholder="Enter promo code" xpath="1">
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
# driver.find_element_by_class_name("promoCode").send_keys("coupon9999")

# 4.
# <button class="promoBtn" xpath="1">Apply</button>
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

# <span class="promoInfo" style="color: green;" xpath="1">Code applied ..!</span>
# print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

# 5.
# <button xpath="1">Place Order</button>
driver.find_element_by_xpath("//button[text()='Place Order']").click()
time.sleep(2)

# 6.
country_menu = driver.find_element_by_tag_name("select")
country_select = Select(country_menu)
country_select.select_by_visible_text("Australia")
print(country_menu.get_attribute("value"))

# <input type="checkbox" class="chkAgree">
agree_term = driver.find_element_by_class_name("chkAgree")
agree_term.click()
print(f"agree_term.is_selected() is {agree_term.is_selected()}")

# <button>Proceed</button>
proceed = driver.find_element_by_xpath("//button[text()='Proceed']")
driver.get_screenshot_as_file('log_files\confirm.png')
proceed.click()
driver.get_screenshot_as_file('log_files\success.png')

time.sleep(10)
driver.close()