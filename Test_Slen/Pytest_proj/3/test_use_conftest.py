import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL_Chrome(BasicTest):
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()
        # ...............................
        # ...............................