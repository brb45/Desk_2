# A callable is anything you can call, using parenthesis, and possibly passing arguments.

# We have a number of callables in Python:
#
# Functions are callables
# Classes are callables
# Methods (which are functions that hang off of classes) are callables
# Instances of classes are NOT callable, but can be turned into callables

# If an object is an instance of some class then it is callable iff it has __call__ attribute.
import time
from datetime import datetime

def main():
    res = 10000 / 3
    print(f"res is {res}")
    print(f"res is {res:8.4}") # width is 8 and decimal places upto 4

    # res is 3333.3333333333335
    # res is 3.333e+03
    start = time.time()
    time.sleep(2)
    stop = time.time()
    print(f"stop time is {stop}") # stop time is 1617236955.5342178
    print(f"stop time is {stop:8.3}")
    # stop time is 1617237749.1253026
    # stop time is 1.62e+09
    delta = stop - start
    print(f'\n(footer_function_scope)--> test duration : {delta:0.5} seconds')

    now_in_second = time.time()
    now_as_obj = time.localtime(now_in_second)
    now_as_str = time.strftime("%H:%M:%S %m/%d/%Y")
    print(now_as_str)

if __name__ == "__main__":
    main()


