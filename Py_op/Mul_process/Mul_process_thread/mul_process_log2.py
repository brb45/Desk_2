from math import sqrt
from timeit import default_timer as timer
import concurrent.futures
import time, os

st_time = time.perf_counter()


def is_prime(x):
    if x < 2:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    input = [i for i in range(10 ** 13, 10 ** 13 + 20000)]
    # concurrent
    start = timer()
    result = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(is_prime, i) for i in input]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                result.append(input[i])

    print('Result 2:', result)
    print('Took: {:.2f} seconds.'.format(timer() - start))

    print("num of cpu is " + str(os.cpu_count()))
    print(os.getpid())
# 8 process: 10 s, 1 process : 35 s, 4 processes: 12.3 s

# 2 process: 63 s
# 4 process: 39.34 s
# 8 process: 35.6
