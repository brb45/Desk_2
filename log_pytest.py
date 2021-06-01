import requests
import pytest, os

@pytest.fixture(scope='function')
def divide_by_zeros():
    return 100/0

def test_1():
    print("\nRun test_1")
    for i in range(10000):
        p = 10
    assert 1 == 1

def test_2():
    print("\nRun test_2")
    # for i in range(10000000000):
    for i in range(100):
        p = 10
    assert 1 == 1

def test_2_1():
    print("run test_2_1")
    a = 1/0
    assert a == 1

def test_2_1_1():
    print("run test_2_1_1")
    assert 1==1
    a = 1/0
    # assert a != 1

def test_2_2():
    try:
        a = 1/0
    except:
        print("Divide by zero")
    assert 1 == 1

def test_2_3(divide_by_zeros):
    print("Run test_2_3")
    assert 1 == 1

def test_2_3_1():
    print("Run test_2_3_1")
    assert 1 == 1
    assert 2 == 1
    assert 3== 3


def test_3():
    print("\nRun test_3")
    for i in range(10000):
        p = 10
    assert 1 == 1

def test_4():
    print("\nRun test_4")
    for i in range(10000):
        p = 10
    assert 1 == 1

# if __name__ == '__main__':
#     # pytest.main(['-sv','-n 3', 'log_test.py'])
#     os.system('pytest -sv log_test.py')
#     print("ALL DONE!!!!")


