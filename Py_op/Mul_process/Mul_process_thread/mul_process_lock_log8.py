import threading
from time import sleep, ctime

lock = threading.Lock()
test_list = [10, 5]

def loop(num_run, nsec):
    lock.acquire()
    print('start run ' + str(num_run) + ' at : ' + str(ctime()) + " for " + str(nsec), " seconds")
    sleep(nsec)
    lock.release()
    print("num_run {} is idle".format(num_run))
    if num_run == 0:
        sleep(nsec)
    print('run ', num_run, ' done at : ', ctime())


def main():
    print('starting at : ', ctime())
    threads = []
    runs = range(len(test_list))

    for run in runs:
        t = threading.Thread(target=loop, args=(run, test_list[run]))
        threads.append(t)

    for i in runs:
        threads[i].start()

    for i in runs:
        threads[i].join()

    print('all DONE at : ', ctime())


if __name__ == '__main__':
    print(5 // 2, 6 % 2, 7 / 2)
    main()
#
# "C:\Users\jsun\My Documents\venv\Scripts\python.exe" C:/Users/jsun/Documents/Py_projects/mul_process/mul_process_log9.py
# 2 0 3.5
# starting at :  Sun May 19 11:05:44 2019
# start run 0 at : Sun May 19 11:05:44 2019 for 10  seconds
# num_run 0 is idle
# start run 1 at : Sun May 19 11:05:54 2019 for 5  seconds
# num_run 1 is idle
# run  1  done at :  Sun May 19 11:05:59 2019
# run  0  done at :  Sun May 19 11:06:04 2019
# all DONE at :  Sun May 19 11:06:04 2019