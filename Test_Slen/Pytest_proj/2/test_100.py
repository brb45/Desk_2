import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    time.sleep(10)
    request.cls.driver = driver
    yield
    driver.close()
    time.sleep(3)

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

class TestBooking(BaseTest):

    def test_search_flight(self):
        self.driver.get("http://www.facebook.com/")
        time.sleep(2)


    def test_choose_any_flight(self):
        self.driver.get("http://www.reuters.com/")
        time.sleep(2)

class Test_2(BaseTest):
    def test_open_url(self):
        url = "https://login.salesforce.com"
        self.driver.get(url)
        time.sleep(1)
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.get_screenshot_as_file('salesforce.png')
        time.sleep(2)

@pytest.mark.usefixtures('driver_init')
class Test_3:
    def test_open_url(self):
        url = "https://www.yahoo.com"
        self.driver.get(url)
        time.sleep(1)
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.get_screenshot_as_file('salesforce.png')
        time.sleep(2)