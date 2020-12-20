#from __future__ import with_statement
import threading
from time import sleep,ctime

lock = threading.Lock()
loops = [4,2]

def loop(nloop,nsec):
    with(lock):
        #lock.acquire()
        print('start loop '+str(nloop)+' at : '+str(ctime()))
        #lock.release()
    sleep(nsec)
    print('loop ',nloop,' done at : ',ctime())

def main():
    print('starting at : ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at : ',ctime())

if __name__ == '__main__':
    main()