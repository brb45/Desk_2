import threading
class Counter():
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
    def increment(self):
        self.lock.acquire()
        old_count = self.count
        self.count = old_count + 1
        self.lock.release()
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

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

trial1 = conduct_trial()
print(trial1)
trial2 = conduct_trial()
print(trial2)
trial3 = conduct_trial()
print(trial3)
'''
200000
200000
200000
'''