# The most basic function in the Python time module is time()

# It returns a floating point value that represents the number of seconds
# that have passed since the epoch. The epoch is a a platform-dependent point where the time starts

import time
t = time.localtime()
print("The struct_time is:", t)
# The struct_time is: time.struct_time(tm_year=2021, tm_mon=4, tm_mday=7, tm_hour=15, tm_min=46, tm_sec=17, tm_wday=2, tm_yday=97, tm_isdst=1)
sec = time.mktime(t) # The number of seconds is: 1617835577.0
print("The number of seconds is:", sec)

# Python time.time()
# The time() function returns the number of seconds passed since epoch.
#
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).

import time
seconds = time.time()
print("Seconds since epoch =", seconds)
# Seconds since epoch = 1617835784.6971433

##
# Python time.ctime()
# The time.ctime() function takes seconds passed since epoch as an argument and
# returns a string representing local time.

import time

# seconds passed since epoch
# seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)
# Local time: Wed Apr  7 15:51:01 2021

##
# Python time.localtime()
# The localtime() function takes the number of seconds passed since epoch
# as an argument and returns struct_time in local time.

import time

result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
# result: time.struct_time(tm_year=2021, tm_mon=4, tm_mday=7, tm_hour=15, tm_min=59, tm_sec=23, tm_wday=2, tm_yday=97, tm_isdst=1)
# year: 2021
# tm_hour: 15

##
# Python time.strftime()
# The strftime() function takes struct_time (or tuple corresponding to it) as an argument and
# returns a string representing it based on the format code used. For example,

# get current time using time.localtime()
import time
named_tuple = time.localtime() # get struct_time of current time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)
# year: 2021
# tm_hour: 16
# 04/07/2021, 16:02:19

time_string = time.strftime("%m:%d:%Y:%H:%M:%S", named_tuple)
time_list = time_string.split(":")
print(time_list) # ['04', '07', '2021', '16', '50', '11']

##
# Current time using datetime object
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S:%d:%m:%Y") # return a string
print("Current Time =", current_time)
# Current Time = 16:53:53:07:04:2021

