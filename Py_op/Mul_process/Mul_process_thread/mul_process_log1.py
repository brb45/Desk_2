import concurrent.futures
import math
import os
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

# ex.map(fun_name, iterable), return an iterator object
def main1():
    with concurrent.futures.ProcessPoolExecutor() as ex:
        for num, rst in zip(PRIMES, ex.map(is_prime, PRIMES)):
            print(num,rst)

def main2():
    with concurrent.futures.ProcessPoolExecutor() as ex:
        for num, rst in enumerate(ex.map(is_prime, PRIMES)):
            print(num, rst)

def main3():
    with concurrent.futures.ProcessPoolExecutor() as ex:
        print(next(ex.map(is_prime, [100])))

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main3()
    print(os.cpu_count())
    print(os.getpid())
