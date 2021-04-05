## 1.
class test( ):
    def __init__(self, nick_name):
        self.nick_name = nick_name

    def callback(self):
        print('self is  ', self)

def main():

    obj = test("log")
    print("obj   is ", obj)
    obj.callback()
    # obj   is  <__main__.test object at 0x03108290>
    # self is   <__main__.test object at 0x03108290>
    print("*****************************************")

    this_test = test(obj)
    this_test.callback() # self is   <__main__.test object at 0x00718D10>
    print("_______________________________________________")

    print("obj.__dict__ is ", obj.__dict__) # {'nick_name': 'log'}
    # obj.__dict__ is  {'nick_name': 'log'}
    # print("_______________________________________________")

#@ 2.
class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1
        #count +=1  , wrong

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

def main_1():
    a = InstanceCounter(5)
    print("val of obj: {a.get_val()}, count: {a.get_count()}")

    b = InstanceCounter(10)
    print("val of obj: {a.get_val()}, count: {b.get_count()}")

    c = InstanceCounter(100)
    print("val of obj: {a.get_val()}, count: {c.get_count()}")

    """
    val of obj: 5, count: 1
    val of obj: 10, count: 2
    val of obj: 100, count: 3
    """

    print("---------------------------------")
    print(a.count) # 3
    print(b.count) # 3
    print(c.count) # 3


if __name__ == "__main__":
    # main()
    # main_1()
#


