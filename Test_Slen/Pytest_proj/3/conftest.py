# Import the 'modules' that are required for execution

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()