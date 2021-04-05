##1. read the last line
fileName = 'file_rw.py'
# 1.1 last line

with open(fileName, 'r', encoding='utf-8') as f:
    last_line = f.readlines()[-1]
    print(last_line)

# 1.2 read last line
import os
# file needs to be open in 'rb'
with open(fileName, 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode()
    print(last_line)

# 1.2.1
import os
# file needs to be open in 'rb'
with open(fileName, 'rb') as f:
    f.seek(-2, 2) # 2 means os.SEEK_END
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode()
    print(last_line)

# 1.3 last line
import subprocess
# line = subprocess.check_output(['tail', '-1', "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\file_rw.py"])
# print(line)