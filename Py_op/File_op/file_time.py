# os.stat


# check file size
import os, time
file_name = "log_IQlite_Flow_Common1.txt"#"Teradyne-Office-365-Training.pdf" #"data.json"
file_size_in_byte = os.path.getsize(file_name)

print(f"file size in byte is {file_size_in_byte}") # 1069626
# file size in byte is 1069626

##
# os.path.getmtime()
# method in Python is used to get the time of last modification of the specified path
# This method returns a floating point value which represents the number of seconds since the epoch

# importing os and time module
import os
import time
from datetime import datetime

# Path
path = file_name

# Get the time of last
# modifation of the specified
# path since the epoch
modification_time = os.path.getmtime(path)
print("Last modification time since the epoch:", modification_time)

# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)

# Last modification time since the epoch: 1537570713.383867
# Last modification time(Local time): Fri Sep 21 15:58:33 2018

file_date = datetime.strptime(local_time, "%a %b %d %H:%M:%S %Y")
print("Last modif: %s" % file_date.strftime('%Y-%m-%d %H:%M:%S'))
# Last modif: 2018-09-21 15:58:33

#os.path.getctime(path) --> time when file is created.

# Get file's Last modification time stamp only in terms of seconds since epoch
modTimesinceEpoc = os.path.getmtime(path)
# Convert seconds since epoch to readable timestamp
modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))
print("Last Modified Time : ", modificationTime )
# Last Modified Time :  2018-09-21 15:58:33