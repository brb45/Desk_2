import threading
import multiprocessing
import time
import math

def countdown(n):
    while n > 0:
        n -= 1

def mult_threads(n):
     t1 = threading.Thread(target= countdown,args=(n//2,))
     # t3 = threading.Thread(target=countdown, args=(n//2,))
     t2 = threading.Thread(target= countdown,args=(n//2,))
     t1.start()
     t2.start()
     print('started')
     t1.join()
     t2.join()
     print("delay ended")
     #time.sleep(2)

def mult_process(n):
    pn1 = multiprocessing.Process(target=countdown,args=(n//2,))
    pn2 = multiprocessing.Process(target=countdown,args=(n//2,))
    pn1.start()
    pn2.start()
    pn1.join()
    pn2.join()

if __name__ == '__main__':
    num = 1000_000_000
    print ('CPU_Cores = :' + str(multiprocessing.cpu_count()))
    #单核串行
    t1_s_time = time.clock()
    countdown(num)
    print ('1 thread 1 Process exec: ', math.floor(time.clock() -t1_s_time))
    #双核2Thread
    t2_s_time = time.clock()
    mult_threads(num)
    print ('2 threads  exec: ', math.floor(time.clock() -t2_s_time))
    #双核2Process
    t3_s_time = time.clock()
    mult_process(num)
    end_time =  time.clock()
    print ('1 Threads 2 Process execTime = ', math.floor(end_time - t3_s_time) )
"""
CPU_Cores = :8
1 thread 1 Process exec:  46
started
delay ended
2 threads  exec:  44
1 Threads 2 Process execTime =  24
"""