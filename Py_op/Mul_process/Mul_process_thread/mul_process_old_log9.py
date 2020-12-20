import threading

balance = 0

def data_operator(n):
    global balance  #
    balance += n
    balance -= n
    # print(balance, "data_operator")

def change_it(n):
    print(n, "change-it")

    def change_it(n):
        for item in range(0, 10 * 6):
            with main_thread_lock:
                data_operator(n)

def thread_synchronization():
    # print(5)
    t1 = threading.Thread(target=change_it, args=(5,))
    t2 = threading.Thread(target=change_it, args=(8,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    global balance
    print(balance)


if __name__ == "__main__":
    thread_synchronization()

# 5 change-it
# 8 change-it
# 0