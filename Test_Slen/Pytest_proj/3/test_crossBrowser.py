# Import the 'modules' that are required for execution for Selenium test automation

import pytest
# import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL_Chrome(BasicTest):
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()

        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == self.driver.title

        sample_text = "Happy Testing at LambdaTest"
        email_text_field = self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)
        time.sleep(5)

        self.driver.find_element_by_id("addbutton").click()
        time.sleep(5)

        output_str = self.driver.find_element_by_name("li6").text
        sys.stderr.write(output_str)

        time.sleep(2)