import threading
import time
class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

# counter = Counter()
# initial_count = counter.get_count()
# count_up_100000(counter)
# final_count = counter.get_count()
# print(final_count)


# counter = Counter()
# #count_thread = threading.Thread(target=count_up_100000, args=[counter])
# count_thread  = threading.Thread(target=count_up_100000, args=(counter,))
# count_thread.start()
# mid_join = counter.get_count()
# count_thread.join()
# after_join = counter.get_count()
# print("mid_join _{}".format(mid_join))
# print(after_join)
#
# mid_join _24695
# 100000
###################################################
# def conduct_trial(i):
#     counter = Counter()
#     count_thread = threading.Thread(target=count_up_100000, args=[counter])
#     count_thread.start()
#     intermediate_value = counter.get_count()
#     count_thread.join()
#     print("i {} --> inter_value {}".format(i, intermediate_value))
#     return intermediate_value
#
# trial1_mid = conduct_trial(1)
# print(trial1_mid)
# trial2 = conduct_trial(2)
# print(trial2)
# trial3 = conduct_trial(3)
# print(trial3)
#
# i 1 --> inter_value 26876
# 26876
# i 2 --> inter_value 22792
# 22792
# i 3 --> inter_value 31161
# 31161

##################################################
# import threading
# def count_up_100000(counter, lock):
#     for i in range(10000):
#         lock.acquire()
#         for i in range(10):
#             counter.increment()
#         lock.release()
#
# def conduct_trial():
#     counter = Counter()
#     lock = threading.Lock()
#     count_thread = threading.Thread(target=count_up_100000, args=[counter, lock])
#     count_thread.start()
#     lock.acquire()
#     intermediate_value = counter.get_count()
#     lock.release()
#     count_thread.join()
#     print(counter.get_count())
#     return intermediate_value
#
# lock = threading.Lock()
# trial1 = conduct_trial()
# print(trial1)
# trial2 = conduct_trial()
# print(trial2)
# trial3 = conduct_trial()
# print(trial3)

# 100000
# 25780
# 100000
# 23630
# 100000
# 24210
#######################################################################
def count_up_100000(counter):
    #lock = threading.Lock()
    for i in range(100000):
        lock.acquire()
        counter.increment()
        lock.release()

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

for i in range(100):
    lock = threading.Lock()
    trial1 = conduct_trial()
    print(trial1)
    #trial2 = conduct_trial()
    #print(trial2)
    #trial3 = conduct_trial()
    #print(trial3)

# 200000
# 200000
# 200000
# 200000
# 200000