import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time, random


def read(q):
    print('Get %s from queue.' % q)
    time.sleep(random.random())


def main():
    futures1 = set()
    with ProcessPoolExecutor() as executor:
        for q in (chr(ord('A') + i) for i in range(26)):
            future = executor.submit(read, q)
            futures1.add(future)
    try:
        for future in concurrent.futures.as_completed(futures1):
            err = future.exception()
            if err is not None:
                raise err
    except KeyboardInterrupt:
        print("stopped by hand")


if __name__ == '__main__':
    main()