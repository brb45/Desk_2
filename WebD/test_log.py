
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

# def test_divide_by_0():
#     with pytest.raises(ZeroDivisionError):
#         1/0
#
# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py', '--resultlog=C:\\Users\jsun\Documents\Desk_2\WebD\\test_log.txt'])


# @pytest.fixture(params=[{'a':100,"c": 100, 'd':200}, {'b':100} , {'c': 500, 'e':600}])
# def pass_dic(request):
#     return request.param
#
# @pytest.mark.usefixtures('pass_dic')
# def test_fix(pass_dic):
#     print(pass_dic)
#     # for k,v in pass_dic.items():
#     #     print(k,':', v)

# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py'])

# test_log.py::test_fix[pass_dic0] a : 0
# c : 1
# d : 2
# PASSED
# test_log.py::test_fix[pass_dic1] b : 100
# PASSED
# test_log.py::test_fix[pass_dic2] c : 500
# e : 600
# PASSED

# @pytest.mark.parametrize('test_input,expected',[('3+5',8),
#                          ('2-1',1),('7*5',30)])
# def test_eval(test_input,expected):
#     assert eval("3+3")==7　　
#     # assert True
#
# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py'])

# import pytest
# test_user_data=['linda','sai','tom']
#
# @pytest.fixture(scope='module')
# def login(request):
#     user=request.param
#     print('打开首页登陆%s'%user)
#     return user
#
#
# #indirect=True是把login当作函数去执行
# @pytest.mark.parametrize('login',test_user_data,indirect=True)
# def test_cart(login):
#     usera=login
#     print('不同用户添加购物车%s'%usera)
#     assert usera!=''
# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py'])



# import pytest
# test_user_data=[
#     {'user':'linda','password':'8888'},
#     {'user':'servenruby','password':'123456'},
#     {'user':'test01','password':''}
# ]
#
# @pytest.fixture(scope='module')
# def login_r(request):
#     #可以通过dict形式,虽然传递一个参数，但通过key的方式可以达到累死传入多个参数的效果
#     user=request.param['user']
#     pwd=request.param['password']
#     print('\n打开首页准备登陆，登陆用户%s,密码%s'%(user,pwd))
#     if pwd:
#         return True
#     else:
#         return False
#
# #这是pytest参数化驱动,indeirect=True是把login_r当作函数去执行
# @pytest.mark.parametrize('login_r',test_user_data,indirect=True)
# def test_cart(login_r):
#     #登陆用例
#     a=login_r
#     print('测试用例中login_r的返回值%s'%a)
#     assert a,'失败原因，密码为空'
#
# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py'])

import pytest
# test_user_data1=[{'user':'linda','password':'888888'},
#                  {'user':'servenruby','password':'123456'},
#                  {'user':'test01','password':''}]
# test_user_data2=[{'q':'中国平安','count':3,'page':1},
#                  {'q':'阿里巴巴','count':2,'page':2},
#                  {'q':'pdd','count':3,'page':1}]
# @pytest.fixture(scope='module')
# def login_r(request):
#     #这是接受不了输入的参数，接收一个参数
#     user=request.param['user']
#     pwd=request.param['password']
#     print('\n用户名:%s,密码:%s'%(user,pwd))
#
# @pytest.fixture(scope='module')
# def query_param(request):
#     q=request.param['q']
#     count=request.param['count']
#     page=request.param['page']
#     print('查询的搜索词%s'%q)
#     return request.param
#
# #这是pytest的数据驱动,indeirect=True是把login_r当作函数去执行
# #从下往上执行
# #两个数据进行组合测试，有3*3个测试用例执行(test_user_data1的个数*test_user_data2的个数
# @pytest.mark.parametrize('query_param',test_user_data2,indirect=True)
# @pytest.mark.parametrize('login_r',test_user_data1,indirect=True)
# def test_login(login_r,query_param):
#     #登陆用例
#     print(login_r)
#     print(query_param)

import pytest
# @pytest.mark.run(order=1)
# def test_01():
#     print('test01')
#
# @pytest.mark.run(order=2)
# def test_02():
#     print('test01')
# @pytest.mark.last
# def test_06():
#     print('test01')
#
# def test_04():
#     print('test01')
#
# def test_05():
#     print('test01')
# @pytest.mark.run(order=3)
# def test_03():
#     print('test01')
#
# if __name__ == "__main__":
#     pytest.main(["-sv", 'test_log.py'])

import pytest

# python -m  pip install -U pytest-ordering
# @pytest.mark.run(order=1)
# def test_9():
#     print('test01')
#
# @pytest.mark.run(order=2)
# def test_02():
#     print('test01')
#
# @pytest.mark.last
# def test_16():
#     print('test01')
#
# def test_05():
#     print('test01')
#
# def test_04():
#     print('test01')
#
# @pytest.mark.run(order=3)
# def test_03():
#     print('test01')
#

## default is warning: DEBUG < INFO < WARNING < ERROR < CRITICAL
# import time
# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
# def test_1():
#     log = logging.getLogger('test_1')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     assert 1, 'should pass'
#
#
# def test_2():
#     log = logging.getLogger('test_2')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     assert 0, 'failing for demo purposes'

# import allure
# import pytest
#
#
# @allure.feature('test_module_01')
# def test_case_01():
#     """
#     用例描述：Test case 01
#     """
#     assert 0
#
#
# @allure.feature('test_module_02')
# def test_case_02():
#     """
#     用例描述：Test case 02
#     """
#     assert 0 == 0
#
# # PS C:\Users\jsun\Documents\Desk_2\WebD> allure generate allure_results --clean -o allureReport
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './allure_results'])
#
# import allure
# import pytest
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# def test_case_01():
#     """
#     用例描述：Test case 01
#     """
#     assert 0
#
# @allure.feature('test_module_01')
# @allure.story('test_story_02')
# def test_case_02():
#     """
#     用例描述：Test case 02
#     """
#     assert 0 == 0
#
#
# import allure
# import pytest
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# @allure.severity('blocker')
# def test_case_01():
#     """
#     用例描述：Test case 01
#     """
#     assert 0
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# @allure.severity('critical')
# def test_case_02():
#     """
#     用例描述：Test case 02
#     """
#     assert 0 == 0
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_02')
# @allure.severity('normal')
# def test_case_03():
#     """
#     用例描述：Test case 03
#     """
#     assert 0
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_02')
# @allure.severity('minor')
# def test_case_04():
#     """
#     用例描述：Test case 04
#     """
#     assert 0 == 0
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './report/xml'])
#
# import allure
# import pytest
#
# @allure.step("字符串相加：{0}，{1}")
# # 测试步骤，可通过format机制自动获取函数参数
# def str_add(str1, str2):
#     if not isinstance(str1, str):
#         return "%s is not a string" % str1
#     if not isinstance(str2, str):
#         return "%s is not a string" % str2
#     return str1 + str2
#
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# @allure.severity('blocker')
# def test_case():
#     str1 = 'hello'
#     str2 = 'world'
#     assert str_add(str1, str2) == 'helloworld'
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './report/xml'])
#
#
#
#
# import allure
# import pytest
#
#
# @allure.step("字符串相加：{0}，{1}")     # 测试步骤，可通过format机制自动获取函数参数
# def str_add(str1, str2):
#     print('hello')
#     if not isinstance(str1, str):
#         return "%s is not a string" % str1
#     if not isinstance(str2, str):
#         return "%s is not a string" % str2
#     return str1 + str2
#
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# @allure.severity('blocker')
# @allure.issue("http://www.baidu.com")
# @allure.testcase("http://www.testlink.com")
# def test_case():
#     str1 = 'hello'
#     str2 = 'world'
#     assert str_add(str1, str2) == 'helloworld'
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './report/xml'])





















# args = ['-s', '-q', 'TestCase/test_Case.py', '--alluredir', xml_report_path, '--clean-alluredir']
# pytest.main(args)
# # --clean清空上一次的html报告
# cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)



#
if __name__ == "__main__":
    pytest.main(["-v", "-capture=no" 'test_log.py'])