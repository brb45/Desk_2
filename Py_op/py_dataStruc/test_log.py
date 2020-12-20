
###14
"""
from multiprocessing import Process, Queue, Pipe
import os

# 一个进程写数据
def write(p):
    for i in range(100):
        print('Write', i)
        p.send(i) # send 方法
    p.close()

# 另一个进程读数据:
def read(p):
    while True:
        value = p.recv() # recv方法
        print('Read', value)

if __name__ == '__main__':

    print('parent process %s is running...' % os.getpid())

    # 父进程创建Pipe，并传给各个子进程：
    pipe = Pipe()
    pw = Process(target=write, args=(pipe[0],))
    pr = Process(target=read, args=(pipe[1],))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # 强行终止

    print('child process stop')
"""
###15
"""
from multiprocessing import Process, Pool
import os
import time


def run_proc(wTime):
    n = 0
    while n < 3:
        print("subProcess %s run," % os.getpid(), "{0}".format(time.ctime()))
        time.sleep(wTime)
        n += 1

if __name__ == "__main__":
    p = Process(target=run_proc, args=(2,))
    p.daemon = True
    p.start()
    p.join()    #加入join方法
    time.sleep(10)
    print("Parent process run. subProcess is ", p.pid)
    print("Parent process end,{0}".format(time.ctime()))

"""
###16
"""
from multiprocessing import Process, Pool
import os
import time

class Myprocess(Process):

    def __init__(self, wTime):
        Process.__init__(self)
        self.wTime = wTime

    def run(self):
        n = 0
        while n < 3:
            print("subProcess %s run," % os.getpid(), "{0}".format(time.ctime()))
            time.sleep(self.wTime)
            n += 1

if __name__ == "__main__":
    p = Myprocess(2)
    p.daemon = True
    p.start()    #自动调用run方法
    p.join()
    print("Parent process run. subProcess is ", p.pid)
    print("Parent process end,{0}".format(time.ctime()))
"""
###17
"""
from multiprocessing import Process,Pool
import os,time

def run_proc(name):        ##定义一个函数用于进程调用
    for i in range(5):
        time.sleep(0.2)    #休眠0.2秒
        print('Run child process %s (%s)' % (name, os.getpid()))
#执行一次该函数共需1秒的时间

if __name__ =='__main__': #执行主进程
    print('Run the main process (%s).' % (os.getpid()))
    mainStart = time.time() #记录主进程开始的时间
    p = Pool(8)           #开辟进程池
    for i in range(16):                                 #开辟14个进程
        p.apply_async(run_proc,args=('Process'+str(i),))#每个进程都调用run_proc函数，
                                                        #args表示给该函数传递的参数。

    print('Waiting for all subprocesses done ...')
    p.close() #关闭进程池
    p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
    print('All subprocesses done')
    mainEnd = time.time()  #记录主进程结束时间
    print('All process ran %0.2f seconds.' % (mainEnd-mainStart))  #主进程执行时间
"""
####18
"""
from multiprocessing import Pool
import os
import time
import random


def child_task(name):
    print('子进程 %s ID是：%s 正在运行' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)  # 随机睡眠一段时间
    end = time.time()
    print('子进程 %s 运行了 %0.2f 秒' % (name, (end - start)))


if __name__ == '__main__':  # 交互模式自动开始执行
    print('当前进程(父进程)ID是：%s' % os.getpid())
    p = Pool(4)  # 创建进程池实例，大小是4个进程
    for i in range(5):  # 循环5次，每次循环都创建一个子进程，大小只有4，则第五个需要等待
        p.apply_async(child_task, args=(i,))  # apply_async方法，传入子进程要执行的函数和函数参数(以元组的形式)
    print('子进程循环创建完毕，正在等待子进程执行。。')
    p.close()  # 关闭进程池，之后就不能添加新的进程了
    p.join()  # 如果有进程池，调用join前必须调用close。（join方法，等待所有子进程执行完毕再往下执行）
    print('所有进程运行完毕')
"""
###19
"""
import os
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('子线程 %s ，ID是：%s' % (name, os.getpid()))

print('当前线程(父线程)的ID是： %s' % os.getpid())
p = Process(target=run_proc, args=('test',))  # 创建Process的实例，并传入子线程要执行的函数和参数
p.start()  # 子线程开始执行
p.join()  # join方法用于线程间的同步，等线程执行完毕后再往下执行
print('子线程执行完毕，回到主线程%s' % os.getpid())
"""
###20
"""
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):  # 写数据
    for value in ['A', 'B', 'C']:
        print('进程 %s 开始写入 %s' % (os.getpid(), value))
        q.put(value)
        time.sleep(random.random())  # 随机睡眠一段时间，开始写入第二个数据


def read(q):  # 读数据
    while True:
        value = q.get(True)
        print('进程 %s 开始读出 %s' % (os.getpid(), value))


if __name__ == '__main__':
    q = Queue()  # 父进程创建Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))  # 传入进程要执行的函数和函数参数
    pr = Process(target=read, args=(q,))

    pw.start()  # 启动子进程pw，写入:
    pr.start()  # 启动子进程pr，读取:(启动之后，就一直循环着尝试读取，直到被中断)
    pw.join()  # 等待pw结束:
    pr.terminate()  # pw进程执行结束后，就中断pr，因为pr进程里是死循环，无法等待其结束，只能强行终止:
"""
###21
"""
import time, threading
def loop():  # 新线程要执行的函数
    print('创建了线程 %s' % threading.current_thread().name)  # current_thread()返回当前线程的名字
    for n in range(5):  # 循环五次 ， 示例代码
        print('线程 %s 循环第 %s 次' % (threading.current_thread().name, n + 1))
        time.sleep(1)  # 暂定1秒
    print('线程 %s 结束' % threading.current_thread().name)

print('最开始线程 %s 正在执行' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 传入线程要执行的函数和线程的名字，如果不指定名字，系统会有默认的线程名字
t.start()
t.join()  # 等待线程执行完毕
print('线程 %s 结束' % threading.current_thread().name)
"""
###22
"""
# No Lock
import threading
import time

balance = 0  # 银行存款:

lock = threading.Lock()
def change_it(n):
    global balance  # 先存后取，结果应该为0 全局变量
    balance = balance + n
    balance = balance - n

def run_thread(n): # 线程执行函数代码
    for i in range(100000):
        lock.acquire()  # 先获取锁
        try:
            change_it(n)
        finally:
            lock.release()  # 放在finally语句中确保一定会执行，将锁释放
            
def run_thread1(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
"""
###23
"""
import threading

def show(num):
    print ('线程 %s 的结果是: %s' % (threading.current_thread().getName(), num))

def test_add():
    result = 0  # 线程私有变量
    for _ in range(10000000):  # 循环1000次 xrange返回的是生成器，range返回的是list，数据量大的时候用xrange
        result += 1
    show(result)  # 调用其他函数的时候，需要将私有变量传递过去

threads = []
for i in range(5):
    threads.append(threading.Thread(target=test_add, name=(i + 1)))  # 创建10个线程
    threads[i].start()
"""
###24
"""
import threading

data = {} # 定义的全局字典

def show():  # 线程所调用函数不用接收参数，直接获取全局字典的值即可
    thread = threading.current_thread()  # 当前线程的实例
    print ('线程 %s 的结果是: %s' % (thread.getName(), data[thread]))

def test_add():
    thread = threading.current_thread()  # 当前线程的实例作为字典的key值
    data[thread] = 0  # 初始结果为0
    #for _ in xrange(1000):
    for _ in range(1000):
        data[thread] += 1
    show()  # 此时再调用其他函数，可不用传递参数


threads = []
for i in range(5):
    threads.append(threading.Thread(target=test_add, name=(i + 1)))  # 创建5个线程
    threads[i].start()
"""
###25
"""
import threading
data = threading.local()  # 获取ThreadLocal实例

def show():
    thread = threading.current_thread()  # 当前线程的实例
    print ('线程 %s 的结果是: %s' % (thread.getName(), data.num))  # 获取ThreadLocal实例value值data.num(key值已经绑定)


def test_add():
    data.num = 0  # 直接给THreadLocal实例添加num属性，并赋值为0,还可有其他私有变量data.a,data.b等
    for _ in range(1000):
        data.num += 1
    show()


threads = []
for i in range(5):
    threads.append(threading.Thread(target=test_add, name=(i + 1)))  # 创建5个线程
    threads[i].start()
"""
###26


"""
from random import randint
from time import sleep
from multiprocessing import Queue
from threading import Thread, Lock, currentThread

lock = Lock()
def writes(queue):
    print("producing object for Q...",)
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print("consumed object from Q... size now", queue.qsize())
    print(currentThread().name)

def writer(queue, loops):
    for i in range(loops):
        lock.acquire()
        writes(queue)
        lock.release()
        sleep(0.1)

def read(queue):
    while queue.qsize() > 0:
        sleep(randint(2, 4))
        lock.acquire()
        readQ(queue)
        lock.release()
        sleep(randint(2, 4))


funcs = [writer, read]
nfuncs = range(5)
"""
###27
"""
def main():
    nloops1 = 100
    q = Queue(1024)

    thread = []
    t = Thread(target=writer, args=(q, nloops1))
    thread.append(t)

    for i in nfuncs:
        t = Thread(target=read, args=(q,))
        thread.append(t)

    for i in range(len(thread)):
        thread[i].start()

    for i in range(len(thread)):
        thread[i].join()

    print("All Done")



if __name__ == '__main__':
    main()

"""
###28
"""
threading.Thread 并没有显式的提供获取线程调用函数返回值的方法，需求自己实现。
使用数据库是一个办法: 可以让子线程将数据写到数据库中，消费线程再去数据库中读取数据；

如果不想用数据库，可以使用类的全局变量来做传递
"""
###29
"""
import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('starting', self.name, 'at:', ctime())
        #apply(self.func, self.args)
        print(self.name, 'finished at:', ctime())



def fun1(x):
    for i in range(x):
        fd = open('1', 'w')
        fd.close()


def fun2(x):
    y = 0
    for i in range(x):
        y += 1


def main():
    print('staring single thread at:', ctime())

    fun1(15000)
    fun2(50000000)
    print( 'finished single thread at:', ctime())
    t1 = MyThread(fun1, (15000,), fun1.__name__)
    t2 = MyThread(fun2, (50000000,), fun2.__name__)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('all done')
if __name__ == '__main__':
    main()
"""
###30
"""
import threading

class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

def count_up_100000(counter, lock):
    for i in range(10000):
        lock.acquire()
        for i in range(10):
            counter.increment()
        lock.release()

def conduct_trial(thread_ID):
    counter = Counter()
    lock = threading.Lock()
    count_thread = threading.Thread(target=count_up_100000, args=[counter, lock])
    count_thread.start()
    print("Thread_ID {} starts".format(thread_ID))
    lock.acquire()
    intermediate_value = counter.get_count()
    lock.release()
    count_thread.join()
    final_value = counter.get_count()
    return final_value

if __name__ == "__main__":
    thread_ID = 1
    trial1 = conduct_trial(thread_ID)
    thread_ID+=1
    print(trial1)
    trial2 = conduct_trial(thread_ID)
    print(trial2)
    thread_ID+=1
    trial3 = conduct_trial(thread_ID)
    print(trial3)
"""
"""
#31
import threading
class Counter():
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
    def increment(self):
        self.lock.acquire()
        old_count = self.count
        self.count = old_count + 1
        self.lock.release()
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

def conduct_trial():
    counter = Counter()
    count_thread1 = threading.Thread(target=count_up_100000, args=[counter])
    count_thread2 = threading.Thread(target=count_up_100000, args=[counter])

    count_thread1.start()
    count_thread2.start()

    count_thread1.join()
    count_thread2.join()

    final_count = counter.get_count()
    return final_count

trial1 = conduct_trial()
print(trial1)
trial2 = conduct_trial()
print(trial2)
trial3 = conduct_trial()
print(trial3)
"""
####32
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Base_DIR is {}".format(BASE_DIR))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

test_id = dict([("wifi",100),("11ax",1),("bt",2)])
MTDB_test = {"MUMU":0, "MUSU":1,"SUSU":2, "SUMU":3}


from pprint import pprint
test = ["wifi", "bt",'ac',"11ax","ad"]

a = [0,1,2,3,4]

import json

dic = {1:"wifi", 2: "BT"}
jstr = json.dumps(dic)
print(jstr)
print(type(jstr))

lt = list(range(5))
print(lt)
for i in lt:
    i = 10
print(lt)

print("s"+"t")

strs = ['wifi','fiwi','wiif','axt', 'xat','a','txa','bh']
print(strs[::-1])
print(strs)

print(5//2)

rsdb = {'mu+mu':'txtx'}
rsdb.update({'mu+SU':'rxrx'})

rdb = [('mumu','txtx'),('sumu','rxtx')]
rsdb.update(rdb)

for (tech, ant) in rsdb.items():
    print(tech,ant)
#print(rsdb)

rsdb_set = set()
rsdb_set.add("musu")
rsdb_set.update({"SUMU"})
print(rsdb_set)

lookup = dict([("a",1),("b",2)])
print(lookup['a'])

import copy
wifi = ["ax",'bt','ac',[1,2]]
wifi1 = wifi[:]
wifi2 = copy.copy(wifi)
wifi3 = copy.deepcopy(wifi)

#wifi.pop()
#wifi.remove("b")
wifi1[-1].append(3)
wifi2[-1].remove(2)
#wifi.remove('c')
#print(wifi,wifi1,wifi2,wifi3,end='\n')

def proc(wifi):
    wifi.append("ad")

proc(wifi)
print(wifi)

a, b = 10, 100
a,b = [10,20],[30,40]
a,b = (10,20),(30,40)
def multi_int(a,b):
    a += b
    print(a)
multi_int(a,b)
print(a)

s = "abc"
it = iter(s)
while True:
    try:
        print(next(it), end=", ")
    except StopIteration:
        del it
        break

r = iter(range(5))
while True:
    try:
        print(next(r),end=", ")
    except StopIteration:
        del r
        break

word_map = {'wifi':1, "bt":2, "ac":3}
iw = iter(word_map.items())
print(next(iw))

test_zp = zip((1,2,3),['wifi','bt','z-series'])
print(test_zp)
print(next(test_zp))

m = map( lambda x, y: max([x,y]), [4,1,7],[3,5,9] )
print(next(m))

lst = ['wifi','ac','mimo']
print(type(list))

print(lst.__class__)
class test:
    def __init__(self,name):
        self.n = name
print(type(test))
a = test('ci')
print(type(a))

class WifiIterState:
    def __init__(self, wifi):
        self.wifi = wifi
        self.index = 0
    def __next__(self,):
        if self.index >= len(self.wifi._data):
            raise StopIteration
        else:
            tmp = self.wifi._data[self.index]
            self.index += 1
            return tmp
class bt:
    def __init__(self, data):
        self.data = data
    def __iter__(self,):
        return WifiIterState(self)

letter = { c:k for c,k in enumerate(range(10))}
print(letter)

def get_s(n):
    for x in range(n):
        yield x**2
print(list(get_s(10)))

from time import time, sleep
def f(m):
    sleep(m)
def g(n):
    sleep(n)

def measure1(func,m):
    t = time()
    func(m)
    print(func.__name__, "take", time() - t)
#measure1(f,1)
#measure1(g,3)

from time import time, sleep
def f(text,text1,sleep_time=1):
    sleep(sleep_time)
    print(text,text1)

def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs )
    print(func.__name__, 'took', time() - t)

#measure(f,2,3,sleep_time=0.3)
#measure(f,0.2)

class DUT:
    ip = '100.1'
    def __init__(self):
        self.name = 4378

print(DUT.ip)
#print(DUT.name)

class test_cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def cal(self):
        return self.a* self.b

wi = test_cal(10,100)
print(wi.cal())
class Engine():
    def start(self):
        pass

    def stop(self):
        pass

class ElectricEngine(Engine):  #
    pass

class V8Engine(Engine):  #
    pass

class Car():
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()

    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()

class RaceCar(Car):  # Is-A Car
    engine_cls = V8Engine

class CityCar(Car):  # Is-A Car
    engine_cls = ElectricEngine

class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    engine_cls = V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()

class Book:
    def __init__(self, title):
        self.title = title
class Ebook(Book):
    def __init__(self,title,pages,format):
        Book.__init__(self,title,pages)
        self.format = format()
class PDFbook(Book):
    def __init__(self,title,pages,format):
        super().__init__(title,pages)
        super(PDFbook,self).__init__(title, pages)
        Book.__init__(self,title,pages)
        self.format = format()

class OddEven:
    def __init__(self, data):
        self.data = data
        self.index =  list(range(0, len(data),2))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self.data[self.index.pop(0)]
        raise StopIteration

nums = [1,2]
num_iter = iter(nums)
print(num_iter)
print(next(num_iter))
print(next(num_iter))
#print(next(num_iter))

print(next(enumerate(range(10),start = 9)))

odd_num = filter(lambda s: s%2, range(10))
print(next(odd_num))

ev_num = filter(lambda s: s%2 == False, range(10))
print(next(ev_num))
print(next(ev_num))
print("generator_fun")
def sq(value = 0):
    while True:
        value  += 1
        yield (value)**2

generator_fun = sq()

for i in range(5):
    print(next(generator_fun),end=", ")

def apply_fun(a,b,fun):
    return fun(a,b)

rst = apply_fun(2,3, lambda x,y : x*y)
print(rst)

a = 1
print(type(a))

print(isinstance(a,int))

from functools import wraps
def func_name(func):
    message = func.__qualname__
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("message is {}".format(message))
        return func(*args, **kwargs)
    return wrapper

@func_name
def adder(x,y):
    return x+y

print(adder(9,10))
print(adder.__wrapped__(100,90))

import urllib.request
my_web = urllib.request.urlopen('http://www.python.org')
print(my_web.read(100))

from math import pi as PI, sin as s, sqrt as sq
print(s(PI/2))
print(int(sq(100)))

import timeit
print(timeit.timeit("""print('a')""", number = 1000))

import profile
profile.run("adder(9,10)")










