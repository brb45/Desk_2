import pytest
# class Testmethod:
#     print("test start")
#     @pytest.mark.parametrize(('name','age'),[("Xiao Ming",'18'),('Li Lei','20'),('Han Meimei',25)])
#     def testa(self,name,age):
#         pytest.assume(1==0)
#         pytest.assume(1==1)
#         pytest.assume(2==0)
#         pytest.assume(3==0)
#
#         print(name+'this year'+ str(age))

#
import allure
import pytest
#
#
@allure.step("第一步")
def step_1():
    step_2()
    print("打开浏览器")
#
#
@allure.step("第二步")
def step_2():
    step_3()
    print("输入URL")


@allure.step("第三步")
def step_3():
    step_4(username='test', password=123456)
    print("输入账号和密码")
    pass


@allure.step('第四步：登录')
def step_4(username, password):
    print("登录")
    print(username, password)

#
@allure.step("第五步")
def test_login():
    step_1()
    pytest.assume(100==100)
import os
if __name__ == "__main__":
    pytest.main(['-s', '-v', '--alluredir', 'C:\\Users\jsun\Documents\Desk_2\\WebD\\allure_results'])
    # os.system("allure generate C:\\Users\jsun\Documents\Desk_2\\WebD\\allure_report -o ./report --clean")

# C:\Users\jsun\Documents\Desk_2\WebD>pytest -v -s --alluredir allure_report
# allure serve allure_report