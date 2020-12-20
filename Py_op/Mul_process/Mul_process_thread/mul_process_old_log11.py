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

def conduct_trial(i):
    counter = Counter()
    count_thread = threading.Thread(target=count_up_100000, args=[counter])
    count_thread.start()
    intermediate_value = counter.get_count()
    count_thread.join()
    print("i {} --> inter_value {}".format(i, intermediate_value))
    return intermediate_value

trial1_mid = conduct_trial(1)
print(trial1_mid)
trial2 = conduct_trial(2)
print(trial2)
trial3 = conduct_trial(3)
print(trial3)
#
# i 1 --> inter_value 26876
# 26876
# i 2 --> inter_value 22792
# 22792
# i 3 --> inter_value 31161
# 31161