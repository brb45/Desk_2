import threading
from time import sleep, ctime
import datetime

loops = [4,2]

def loop(nloop, nsec):
    print("start loop" + str(nloop) + "at: " + str(ctime()))
    sleep(nsec)
    print("loop {} is done at {}".format(nloop, ctime()))
#
def main():
    print("starting at: {}".format(ctime()))
    threads =[]
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print("all Set {}".format(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))

if __name__ == '__main__':
    main()