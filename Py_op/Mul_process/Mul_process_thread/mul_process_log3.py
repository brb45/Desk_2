from math import sqrt
from timeit import default_timer as timer
import concurrent.futures
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


def main():
  input = [ i for i in range( 10 ** 13, 10 ** 13 + 500)]
  #start = timer()
  #result = [ i for i in input if is_prime(i)]
  #print("it took {:.2f} sec.".format(timer() - start))

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

def main1():
  input = [i for i in range(100)]
  # input = [ i for i in range( 10 ** 13, 10 ** 13 + 500)]

  # concurrent
  start = timer()
  result = []
  with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(is_prime, i) for i in input]
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        # print(i, type(future)) # 491 <class 'concurrent.futures._base.Future'>
        # print(i, future.result()) # 492 False
        if future.result():
            print(i, future.result(), end=", ")
    # 50
    # True, 60
    # True, 128
    # True, 182
    # True, 258
    # True, 266
    # True, 272
    # True, 278
    # True, 282
    # True, 296
    # True, 342
    # True, 389
    # True, 410
    # True, 428
    # True, 452
    # True, 499
    # True
  print('Took: {:.2f} seconds.'.format(timer() - start))


def main2():
    input = [i for i in range(100)]

    # concurrent
    start = timer()
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        running = [ex.submit(is_prime, i) for i in input]
        running_rst = concurrent.futures.as_completed(running)

        for i, rst in enumerate(running_rst):
            if rst.result():
                print(i, rst.result(), end=", ")
    print("test time lasts {}".format(timer() - start))

if __name__ == "__main__":

   main1()




# 8 process: 10 s, 1 process : 35 s, 4 processes: 12.3 s

  # def concurrent_f(x):
  #   global result
  #   result = f(result)
  #
  # result = 3
  #
  # with concurrent.futures.ThreadPoolExecutor(max_workers=20) as exector:
  #   futures = [exector.submit(concurrent_f, i) for i in range(20)]
  #
  #   _ = concurrent.futures.as_completed(futures)
  #
  # print('Result is very large. Only printing the last 5 digits:', result % 100000)
  # print('Concurrent took: %.2f seconds.' % (timer() - start))

