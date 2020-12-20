
from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
import os
import time

def task(n):
    print('{} is running'.format(os.getpid()))
    i = 10
    time.sleep(i)
    print("test wait {} sec".format(i))
    return n ** 2

def solute(res):
    print('solute', res.result())

if __name__ == '__main__':
    p = ThreadPoolExecutor(max_workers=4)  # 进程池
    for i in range(10):
        p.submit(task, i).add_done_callback(solute)  # 按位置传参
    print('主程序')
    for i in range(1,5):
        time.sleep(i)
        print("{} sec later".format(i))