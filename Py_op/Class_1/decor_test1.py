from time import time, sleep
# test_1
def ff(sleep_time=0.1):
    sleep(sleep_time)

def measure_diff_ff(func_obj, *args, **kwargs):
    t = time()
    func_obj(*args, **kwargs)
    print(f"{func_obj.__name__} took {time() - t}")
    # measure_diff_ff(ff, 0.2)
    # measure_diff_ff(ff, sleep_time=0.3)
# ff took 0.2
# ff took 0.3

def test_1():
    measure_diff_ff(ff)
    print("------------")
    measure_diff_ff(ff, 0.2)
    print("------------")
    measure_diff_ff(ff, sleep_time=0.6)

# test2
# work_version: 1
def measure_decorator(func_object,*args, **kwargs):
    def wrapper():
        t = time()
        func_object(*args, **kwargs)
        print("{} through decorator took {:.1f}".format(func_object.__name__, time() - t))
    return wrapper

# work_version: 2
def measure_decorator1(func_object):
    def wrapper(*args, **kwargs):
        t = time()
        func_object(*args, **kwargs)
        print("{} through decorator took {:.1f}".format(func_object.__name__, time() - t))
    return wrapper

# DO NOT WORK
def measure_decorator2(func_object):
    def wrapper():
        t = time()
        func_object(*args, **kwargs)
        print("{} through decorator took {:.1f}".format(func_object.__name__, time() - t))
    return wrapper

@measure_decorator
def fo(sleep_time=0.1):
    sleep(sleep_time)

def test2():
    print(fo())

# # ***********************************************
if __name__ == "__main__":
    # test_1()
    # test2()





    # measure_diff(f) # f took 0.3
    # measure_diff(g) # f took 0.8
    # print("______________________________________")
    # measure_diff_ff(ff, 0.2)
    # measure_diff_ff(ff, sleep_time=0.3)
    # print("======================================")
    # print("calling decorator")
    # fff = measure_decorator(fff) # decoration point
    # fff(.5)
    # print("**************************************")
    # ffff(2)
    # ffff(sleep_time=4)