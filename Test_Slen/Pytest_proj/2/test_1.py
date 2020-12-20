import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

class TestBooking(BaseTest):

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.get("http://blazedemo.com/")
        # < input type = "submit" class ="btn btn-primary" value="Find Flights" >
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()

    # < h3 > Flights from Paris to Buenos Aires: < / h3 >
        text = "Travel The World"
        assert self.driver.find_element_by_xpath("//a[@href='index.php']").text == text

    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        assert text == "Your flight from TLV to SFO has been reserved."