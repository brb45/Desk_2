import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)

@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

@pytest.mark.incremental
class TestBooking(BaseTest):

    @pytest.mark.parametrize('url', ["http://blazedemo.com/"])
    def test_search_flight(self, url):
        wait = WebDriverWait(self.driver, 30)
        self.driver.get(url)
        # < input type = "submit" class ="btn btn-primary" value="Find Flights" >
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()

    # < h3 > Flights from Paris to Buenos Aires: < / h3 >
        text = "Travel The World"
        assert self.driver.find_element_by_xpath("//a[@href='index.php']").text == text

    def test_choose_any_flight(self):
        self.driver.get("http://blazedemo.com/")
        wait = WebDriverWait(self.driver, 100)
        # < input type = "submit" class ="btn btn-primary" value="Find Flights" >
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        assert text == "Your flight from TLV to SFO has been reserved."

@pytest.mark.incremental
class TestBooking_2(BaseTest):

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.get("http://blazedemo.com/")
        # < input type = "submit" class ="btn btn-primary" value="Find Flights" >
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()

    # < h3 > Flights from Paris to Buenos Aires: < / h3 >
        text = "Travel The World"
        assert self.driver.find_element_by_xpath("//a[@href='index.php']").text != text
        print("Seems like you have booked incorrect flight!")

    def test_choose_any_flight(self):
        self.driver.get("http://blazedemo.com/")
        wait = WebDriverWait(self.driver, 100)
        # < input type = "submit" class ="btn btn-primary" value="Find Flights" >
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()

        # But what if I want to check that a test fails with expected error? No problem, PyTest can handle this.
        text = self.driver.find_element_by_tag_name("h2").text
        with pytest.raises(AssertionError):
            assert text != "Your flight from TLV to SFO has been reserved."
        print("Seems like you have booked incorrect flight!")

# pytest --html=report.html