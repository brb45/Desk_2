import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("\ntest_fixtureDemo")

    def test_fixtureDemo1(self):
        print("\ntest_fixtureDemo1")

    def test_fixtureDemo2(self):
        print("\ntest_fixtureDemo2")

    def test_fixtureDemo3(self):
        print("\ntest_fixtureDemo3")
        print("\n________________________")

class TestFollowUp:

    def test_setup(self):
        print("\ntest_setup")

    def test_setup1(self):
        print("\ntest_setup1")

    def test_setup2(self):
        print("\ntest_setup2")

    def test_setup3(self):
        print("\ntest_setup3")
        print("\n@@@@@@@@@@@@@@@@@@@@@")

@pytest.mark.usefixtures('setup')
def test_single_function():
    print("\nNot a class")
    print("\n*************************")

def test_include_fixture(setup):
    print("\ntest_include_fixture")