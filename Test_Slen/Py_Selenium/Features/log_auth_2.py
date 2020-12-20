from selenium.webdriver.common.by import By

class LoginPage():
    self.username_field = (By.CSS_SELECTOR, "#login-username")
    # driver.find_element_by_css_selector("#login-username").send_keys(user)
    self.next_button    = (By.XPATH, "//input[@name='signin']")
    # driver.find_element_by_xpath("//input[@name='signin']").click()

    self.password_field = (By.CSS_SELECTOR, "#login-passwd")
    # driver.find_element_by_css_selector("#login-passwd").send_keys(passwd)


    self.submit_btn     = (By.CSS_SELECTOR, "button[name='verifyPassword']")
    # next_button = driver.find_element_by_css_selector("button[name='verifyPassword']")


    create_acct_link = (By.LINK_TEXT, 'Create an account')
    message = (By.CSS_SELECTOR, "#auth-message")

    def test_log_in(self):




class CreateAccountPage():
    header = (By.CSS_SELECTOR, "#header")