import threading

money = 0  # 变量 money 被 t1和 t2 两个线程共享


# 存钱
def put_money(sum):
    global money
    money += sum


# 取钱
def get_money(sum):
    global money
    money -= sum


def run_thread(sum):
    for i in range(1000000):  # 执行的次数要足够多
        # 先存sum，后取sum，钱数应当为0
        put_money(sum)
        get_money(sum)


t1 = threading.Thread(target=run_thread, args=(100,))
t2 = threading.Thread(target=run_thread, args=(1000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(money)