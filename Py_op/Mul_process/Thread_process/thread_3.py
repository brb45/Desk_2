
from time import ctime
import threading

def coding(language):
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print('I\'m coding ',language, ' program at ', ctime() )

def music():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print('I\'m listening music at ', ctime())

if __name__ == '__main__':

    print('thread %s is running...' % threading.current_thread().name)

    thread_list = []
    t1 = threading.Thread(target=coding, args=('Python',))
    t2 = threading.Thread(target=music)
    thread_list.append(t1)
    thread_list.append(t2)

    for t in thread_list:
        t.setDaemon(True)  # 设置为守护线程
        t.start()
        #print('thread %s is running...' % threading.current_thread().name)
        t.join()  # 在这个子线程完成运行之前，主线程将一直被阻塞

    print('thread %s ended.' % threading.current_thread().name)

# thread MainThread is running...
# thread Thread-1 is running...
# I'm coding  Python  program at  Sun May 19 17:29:47 2019
# I'm coding  Python  program at  Sun May 19 17:29:47 2019
# I'm coding  Python  program at  Sun May 19 17:29:47 2019
# I'm coding  Python  program at  Sun May 19 17:29:47 2019
# I'm coding  Python  program at  Sun May 19 17:29:47 2019
# thread Thread-2 is running...
# I'm listening music at  Sun May 19 17:29:47 2019
# I'm listening music at  Sun May 19 17:29:47 2019
# I'm listening music at  Sun May 19 17:29:47 2019
# I'm listening music at  Sun May 19 17:29:47 2019
# I'm listening music at  Sun May 19 17:29:47 2019
# thread MainThread ended.