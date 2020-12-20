# Import the 'modules' that are required for execution
# pytest --capture=no --verbose --html=pytest_selenium_test_report.html test_crossBrowser_1.py
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.mark.parametrize(
    "test_browser, test_url",
    [
        ("chrome", "https://www.lambdatest.com/"),
        ("firefox", "https://www.lambdatest.com/blog/"),
    ]
)
def test_open_url(test_browser, test_url):
    if test_browser == "chrome":
        web_driver = webdriver.Chrome()
        expected_title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
    if test_browser == "firefox":
        web_driver = webdriver.Firefox()
        expected_title = "LambdaTest | A Cross Browser Testing Blog"

    web_driver.get(test_url)
    web_driver.maximize_window()

    assert expected_title == web_driver.title

    time.sleep(5)

    web_driver.close()