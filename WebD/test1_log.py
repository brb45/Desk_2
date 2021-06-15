
# import pytest
# @pytest.fixture() # fixture标记的函数可以应用于测试类外部
# def before():
#     print("------->before")
#     return 100
# @pytest.mark.usefixtures("before")
# class Test_ABC:
#     def setup(self):
#         print("------->setup")
#     def test_a(self,before):
#         print("------->test_a")
#         print(before)
#         assert 100 == before
#
#     def test_b(self):
#         print("------->test_b")


import pytest


# @pytest.fixture(params=[1, 2, 3])
# def need_data(request):  # 传入参数request 系统封装参数
#     return request.param  # 取列表中单个值，默认的取值方式
#
#
# class Test_ABC:
#
#     def test_a(self, need_data):
#         print("------->test_a")
#         assert need_data != 3  # 断言need_data不等于3

# if __name__ == '__main__':
#     pytest.main(["-s","log_test.py"])


import pytest
@pytest.fixture(autouse=True) # 作用域设置为function，自动运行
def before():
    print("------->before")
class Test_ABC:
    def setup(self):
        print("------->setup")
    def test_a(self):
        print("------->test_a")
        assert 1
    def test_b(self):
        print("------->test_b")
        assert 1
if __name__ == '__main__':
    pytest.main(["-sq", "log_test.py"])





