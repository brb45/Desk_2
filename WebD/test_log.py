
import pytest
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


# import pytest
# @pytest.fixture(params=[1, 2, 3, 4, 3, 4,3])
# def need_data(request):  # 传入参数request 系统封装参数
#     return request.param  # 取列表中单个值，默认的取值方式
#
#
# class Test_ABC:
#
#     def test_a(self, need_data):
#         print("------->test_a")
#         assert need_data != 3  # 断言need_data不等于3
#
# if __name__ == '__main__':
#     # pytest.main(["-svx", "test_log.py"]) # -x stop when fails once
#     # pytest.main(["-sv", '--maxfail=2', "test_log.py"]) # --maxfail=2, stop the test once failing twice
#     pytest.main(["-sv","test_log.py"])


# import pytest
# @pytest.fixture(autouse=True) # 作用域设置为function，自动运行
# def before():
#     print("------->before")
# class Test_ABC:
#     def setup(self):
#         print("------->setup")
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#     def test_b(self):
#         print("------->test_b")
#         assert 1
# if __name__ == '__main__':
#     pytest.main(["-sv", "log_test.py"])


# // 指定自定义的或额外的插件?
# content of myinvoke.py
# import pytest
# class MyPlugin(object):
#     def pytest_sessionfinish(self):
#         print("*** test run reporting finishing")
#
#
# pytest.main(["-qq"], plugins=[MyPlugin()])

# import pytest
# def test():
#     val = 10
#
#     assert val % 2  != 0, "not == 0"
# if __name__ == "__main__":
#     pytest.main(["-sv", "test_log.py"])

def test_divide_by_0():
    with pytest.raises(ZeroDivisionError):
        1/0

if __name__ == "__main__":
    pytest.main(["-sv", 'test_log.py', '--resultlog=C:\\Users\jsun\Documents\Desk_2\WebD\\test_log.txt'])
