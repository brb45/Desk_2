import pytest
class Testmethod:
    @pytest.mark.parametrize(('name','age'),[("Xiao Ming",'18'),('Li Lei','20'),('Han Meimei',25)])
    def test_a(self,name,age):
        print(name+'this year'+ str(age))

