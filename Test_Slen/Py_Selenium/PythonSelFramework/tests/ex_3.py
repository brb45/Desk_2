import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        # define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_action_chains_hover_over_menu(self):
        driver = self.driver
        # navigate to the demo website
        driver.get('http://jqueryui.com/menu/')
        time.sleep(3)
        # define Frame
        frame = driver.find_element_by_tag_name('iframe')
        # Switch to the frame
        driver.switch_to_frame(frame)
        # define menu element
        menu_element = driver.find_element_by_id("ui-id-10")
        # define sub menu element
        sub_menu_element = driver.find_element_by_xpath("//ul/li[text()='Perch']")
        # define Action Chains
        action1 = ActionChains(driver)
        action1.move_to_element(menu_element)
        action1.perform()
        # Sleep
        time.sleep(5)
        # verify that sub menu is displayed
        self.assertTrue(sub_menu_element.is_displayed())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()