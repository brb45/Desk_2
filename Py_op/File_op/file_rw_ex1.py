import os

# os.SEEK_SET - beginning of the file
# os.SEEK_CUR - current position
# os.SEEK_END - end of file

# fh.seek(0, os.SEEK_SET)  - go to the beginning of the file.
# fh.seek(0, os.SEEK_END)  - go to the end of the file.

filename = 'file_rw_ex1.txt'
with open(filename, 'w') as fh:
    fh.write('Hello World!\nHow are you today?\nThank you!')

print(os.path.getsize(filename))  # 44

with open(filename,'rb') as fh:
    print(fh.tell())  # 0
    row = fh.readline()
    print(row)  # b'Hello World!\r\n'
    print(fh.tell())  # 14

    fh.seek(-7, os.SEEK_CUR)
    print(fh.tell())  # 7

    row = fh.readline()
    print(row)  # b'orld!\r\n'
    print(fh.tell())  # 14

    # fh.seek(0, os.SEEK_SET)
    fh.seek(0)
    print(fh.tell())  # 0
    print(fh.read(5))  # b'Hello'

    fh.seek(-4, os.SEEK_END)
    print(fh.tell())  # 40
    print(fh.read())  # b'you!'
    print(fh.tell())  # 44

    fh.seek(-1, os.SEEK_END)
    print(fh.tell())  # 43
    print(fh.read())  # b'!'
    print(fh.tell())  # 44

