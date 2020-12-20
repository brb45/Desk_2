import pytest


@pytest.fixture(scope="class")
def setup():
    print("\nI will be executing first")
    yield
    print("\nI will execute last")


@pytest.fixture()
def dataLoad():
    print("\nThree tests have been created!")
    return ["Test_0","Test_1","Test_2"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","shetty"), ("IE","SS")])
def crossBrowser(request):
    return request.param
