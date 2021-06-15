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
    pytest.main(["-vs", "-result=C:\\Users\\jsun\\Documents\\Desk_2\\log_test.log", "log_test.py"])