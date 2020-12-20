import pytest
from unnecessary_math import multiply


# def setup_module(module):
#     print("\nsetup_module      module: {}\n".format(module.__name__))

# # def setup_module():
# #     print("\nI am just a dummy setup\n")

# def teardown_module(module):
#     print("\nteardown_module   module: {}\n".format(module.__name__))


# def setup_function(function):
#     print("\nsetup_function    function: {}\n".format(function.__name__))


# def teardown_function(function):
#     print("\nteardown_function function: {}\n".format(function.__name__))


# def test_numbers_3_4():
#     print("test_numbers_3_4  <============================ actual test code\n")
#     assert multiply(3, 4) == 12


# def test_strings_a_3():
#     print("test_strings_a_3  <============================ actual test code\n")
#     assert multiply('a', 3) == 'aaa'


class TestUM:

    def setup(self):
        print("\nsetup             class:TestStuff")
    def teardown(self):
        print("\nteardown          class:TestStuff")

    def setup_class(cls):
        print("\nsetup_class       class:%s" % cls.__name__)
    def teardown_class(cls):
        print("\nteardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print("\nsetup_method      method:%s" % method.__name__)
    def teardown_method(self, method):
        print("\nteardown_method   method:%s" % method.__name__)

    def test_numbers_5_6(self):
        print('\ntest_numbers_5_6  <============================ actual test code')
        assert multiply(5, 6) == 30
    def test_strings_b_2(self):
        print('\ntest_strings_b_2  <============================ actual test code')
        assert multiply('b', 2) == 'bb'


# (01) C: \Users\jsun\Documents\Py_projects\Pytest_proj\01\pytest_proj5 > python - m pytest - v - s
# == == == == == == == ========================================== test session starts =========================================================
# platform win32 - - Python 3.7.2, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 - - C: \Users\jsun\Documents\Py_projects\Pytest_proj\01\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C: \Users\jsun\Documents\Py_projects\Pytest_proj\01\pytest_proj5
# plugins: bdd-3.1.1, cov-2.7.1, forked-1.0.2, xdist-1.29.0
# collecting ... module is imported pytest_proj5
# importlib.reload(pytest_proj5
#                  C: \Users\jsun\Documents\Py_projects\Pytest_proj\01\pytest_proj5
#                  import pytest_proj4.test_xfail_skip.py
#                  Hello
#                  runns only when import test_mod is imported
#                  module is imported pytest_proj5.test_mod, script name is C: \Users\jsun\Documents\Py_projects\Pytest_proj\01\lib\site-packages\pytest.py
#                  importlib.reload(pytest_proj5.test_mod
#                                   collected 4 items

#                                   test_fixture_class_func.py: : test_numbers_3_4
#                                   setup_module      module: pytest_proj5.test_fixture_class_func
#                                   setup_function    function: test_numbers_3_4

#                                   test_numbers_3_4 <= == == == == == == == == == == == == ===actual test code
#                                   PASSED
#                                   teardown_function function: test_numbers_3_4


#                                   test_fixture_class_func.py: : test_strings_a_3 setup_function    function: test_strings_a_3

#                                   test_strings_a_3 <= == == == == == == == == == == == == ===actual test code
#                                   PASSED
#                                   teardown_function function: test_strings_a_3


#                                   test_fixture_class_func.py: : TestUM: : test_numbers_5_6
#                                   setup_class class: TestUM

#                                   setup_method      method: test_numbers_5_6

#                                   setup class: TestStuff

#                                   test_numbers_5_6 <= == == == == == == == == == == == == ===actual test code
#                                   PASSED
#                                   teardown class: TestStuff

#                                   teardown_method   method: test_numbers_5_6

#                                   test_fixture_class_func.py: : TestUM: : test_strings_b_2
#                                   setup_method      method: test_strings_b_2

#                                   setup class: TestStuff

#                                   test_strings_b_2 <= == == == == == == == == == == == == ===actual test code
#                                   PASSED
#                                   teardown class: TestStuff

#                                   teardown_method   method: test_strings_b_2

#                                   teardown_class class: TestUM

#                                   teardown_module   module: pytest_proj5.test_fixture_class_func


#                                   == == == == == == == == == == == == == == == == == == == == == == == == == == == 4 passed in 0.09 seconds == == == == == == == == == == == == == == == == == == == == == == == == == == ==
