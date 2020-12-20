#read() return a string for the whole file
#read(n) return content of n bytes, upto 5555 bytes

#readlines(n): read in n bytes or upto the line where the n-byte in
# if the last byte is part of a line, that whole line will be returned as the last line.

# readline(n): return a string of n bytes, if n < # of bytes of the first line
# return the first line if n >= # of bytes of the first line

## 1. readlines(n_byte)
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_test.txt"
with open(file_name, "r") as f:
    lines = f.readlines(36)  #
    print(lines)
# ['2018-02-10 18:33:52,527 - DEBUG- End\n']

with open(file_name, "r") as f:
    lines = f.readlines(37)  #
    print(lines)
    # ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n']

## 2. read(n_byte): read upto n byte
with open(file_name, 'r') as infile:
    text = infile.read(36)
    print(text)
    # 2018 - 02 - 10 18: 33:52, 527 - DEBUG - End

with open(file_name, 'r') as infile:
    text = infile.read(38)
    print(text)
    # 2018 - 02 - 10 18: 33:52, 527 - DEBUG - End
    # 2

## 3.
##  splitlines() return a list of lines, stripped of "\n"
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_test.txt"
with open(file_name, 'r') as infile:
    text = infile.read().splitlines()  # a list of strings stripped of "\n"
    print(text)
    # ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log',
     # '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']

## 4. Read Big text files to process lines
# use readlines(n_byte) is a good choice
#
# i have a large text file (~7 GB). I am looking if exist the fastest way to read large text file.
# I have been reading about using several approach as read chunk-by-chunk in order to speed the process.

file = open("sample.txt")
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        pass  # do something**strong text**

# in order to process 96, 900 lines of text per second.Other authors suggest to use islice()

from itertools import islice
with open(...) as f:
    while True:
        next_n_lines = list(islice(f, n))
        if not next_n_lines:
            break
        # process next_n_lines

file_rd = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_long.txt"

from itertools import islice
with open(file_rd) as f:
    while True:
        n = 3
        next_n_lines = list(islice(f, n))
        if next_n_lines:
            print(next_n_lines, "\n-----------")
        else:
            break

# ______________________________________
#
# [' 2018-02-10 18:33:52,526 - DEBUG- Start of program\n', ' 2018-02-10 18:33:52,526 - DEBUG- Start of factorial(3)\n', ' 2018-02-10 18:33:52,526 - DEBUG- i is 1, total is 1\n']
# -----------
# [' 2018-02-10 18:33:52,526 - DEBUG- i is 2, total is 2\n', ' 2018-02-10 18:33:52,527 - DEBUG- i is 3, total is 6\n', ' 2018-02-10 18:33:52,527 - DEBUG- End of factorial(3)\n']
# -----------
# [' 2018-02-10 18:33:52,527 - DEBUG- End of program\n', ' 2018-02-10 18:33:52,527 - INFO- The logging module is working.\n', ' 2018-02-10 18:33:52,527 - WARNING- An error message is about to be logged.\n']
# -----------
# [' 2018-02-10 18:33:52,527 - ERROR- An error has occurred.\n', ' 2018-02-10 18:33:52,527 - CRITICAL- The program is unable to recover!\n', ' 2018-02-26 14:56:35,784 - DEBUG- Start of program\n']
# -----------
# [' 2018-02-26 14:56:35,784 - DEBUG- Start of factorial(3)\n', ' 2018-02-26 14:56:35,784 - DEBUG- i is 1, total is 1\n', ' 2018-02-26 14:56:35,784 - DEBUG- i is 2, total is 2\n']
# -----------
# [' 2018-02-26 14:56:35,784 - DEBUG- i is 3, total is 6\n', ' 2018-02-26 14:56:35,784 - DEBUG- End of factorial(3)\n', ' 2018-02-26 14:56:35,784 - DEBUG- End of program\n']
# -----------
# [' 2018-02-26 14:56:35,784 - INFO- The logging module is working.\n', ' 2018-02-26 14:56:35,784 - WARNING- An error message is about to be logged.\n', ' 2018-02-26 14:56:35,784 - ERROR- An error has occurred.\n']
# -----------
# [' 2018-02-26 14:56:35,784 - CRITICAL- The program is unable to recover!\n', ' 2018-02-26 14:57:00,270 - DEBUG- Start of program\n', ' 2018-02-26 14:57:00,270 - DEBUG- Start of factorial(3)\n']
# -----------
# [' 2018-02-26 14:57:00,270 - DEBUG- i is 1, total is 1\n', ' 2018-02-26 14:57:00,270 - DEBUG- i is 2, total is 2\n', ' 2018-02-26 14:57:00,270 - DEBUG- i is 3, total is 6\n']
# -----------
# [' 2018-02-26 14:57:00,270 - DEBUG- End of factorial(3)\n', ' 2018-02-26 14:57:00,270 - DEBUG- End of program\n', ' 2018-02-26 14:57:00,270 - INFO- The logging module is working.\n']
# -----------
# [' 2018-02-26 14:57:00,270 - WARNING- An error message is about to be logged.\n', ' 2018-02-26 14:57:00,270 - ERROR- An error has occurred.\n', ' 2018-02-26 14:57:00,270 - CRITICAL- The program is unable to recover!\n']
# -----------





