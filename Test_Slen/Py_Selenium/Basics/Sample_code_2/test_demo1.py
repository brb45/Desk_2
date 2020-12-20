# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

    # @pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("Firefox", "shetty"), ("IE", "SS")])
    # def crossBrowser(request):
    #     return request.param







