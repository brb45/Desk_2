import pytest

@pytest.fixture(params=[{'first': 100}, "third"], scope='module')
def qa_data(request):
    print("\n***** starting fixture session *****")
    print(f"\ntype of request.param is {type(request.param)}")
    print(f'request.param is {request.param}')
    print("***** Ending   fixture session *****")
    return request.param

@pytest.fixture(params=[("offer", "tuple"), ["check", 'balance']])
def qa_data_1(request):
    print("\n@@@@@ starting fixture session @@@@@")
    print(f"\ntype of request.param is {type(request.param)}")
    print(f'request.param is {request.param}')
    print("@@@@@ Ending   fixture session @@@@@")
    return request.param

print("----------------------------------------------")
def test_fixture_params(qa_data):
    print(f"type of qa_data is {type(qa_data)}")
    print(f"qa_data is {qa_data}")


@pytest.mark.usefixtures('qa_data')
def test_fixture():
    print("\nDone")


def test_fixture_params_1(qa_data_1):
    print(f"type of qa_data is {type(qa_data_1)}")
    print(f"qa_data is {qa_data_1}")


@pytest.mark.usefixtures('qa_data_1')
def test_fixture_1():
    print("\nCompleted!")














