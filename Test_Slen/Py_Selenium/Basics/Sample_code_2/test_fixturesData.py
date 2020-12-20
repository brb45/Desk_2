import pytest

from .BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_run_setup(self, setup):
        print("calling setup")

    def test_editProfile(self, dataLoad):
        log = self.getLogger()

        log.info(dataLoad[0])
        log.debug(dataLoad[1])
        log.warning(dataLoad[2])
        log.error(dataLoad[0])
        log.critical(dataLoad[1])

        print(f"this is {dataLoad[2]}")














# @pytest.fixture()
# def dataLoad():
#     print("user profile data is being created")
#     return ["Rahul","Shetty","rahulshettyacademy.com"]




