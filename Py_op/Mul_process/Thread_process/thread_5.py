from multiprocessing import Process, Queue
import os

# 一个进程写数据
def write(q):
    for i in range(100):
        print('Write', i)
        q.put(i)

# 另一个进程读数据:
def read(q):
    while True:
        value = q.get(True)
        print('Read', value)

if __name__ == '__main__':

    print('parent process %s is running...' % os.getpid())

    # 在父进程中创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate() # 强行终止pr进程

    print('child process stop')