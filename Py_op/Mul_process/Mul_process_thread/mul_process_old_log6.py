########
import multiprocessing
import random
import time
########
def read(q):
    while True:
        try:
            value = q.get()
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        finally:
            q.task_done()

def main():
    q = multiprocessing.JoinableQueue()
    pw1 = multiprocessing.Process(target=read, args=(q,))
    pw2 = multiprocessing.Process(target=read, args=(q,))
    pw1.daemon = True
    pw2.daemon = True
    pw1.start()
    pw2.start()
    for c in [chr(ord('A')+i) for i in range(26)]:
        q.put(c)
    try:
        q.join()
    except KeyboardInterrupt:
        print("stopped by hand")

if __name__ == '__main__':
    main()
########
