from shutil import copyfile, copy2 # copytree
import os
import shutil

# with open(file, "r") as fin:
# doesn't read the whole file into memory, which solves the problem with files too big to fit in memory

# ijson will iteratively parse the json file instead of reading it all in at once. This is slower
# than directly reading the whole file in, but it enables us to work with large files that can’t fit in memory.
# To use ijson, we specify a file we want to extract data from, then we specify a key path to extract:

#
# with is the nice and efficient pythonic way to read large files. advantages:
# 1) file object is automatically closed after exiting from with execution block.
# 2) exception handling inside the with block.
# 3) memory for loop iterates through
# the f file object line by line. internally it does buffered IO (to optimized on costly IO operations) and memory management.

# windows打开文件默认是以“gbk“编码的，可能造成不识别unicode字符，于是做了如下的修改：
# Just add: encoding='utf-8'
# self.file = open('biaobai.json', 'w', encoding="utf-8")
# self.file.write(content)

# read one line at a time (with open) file_handle
with open("x.txt") as f:
    for line in f:
        do something with data

import ijson
filename = "md_traffic.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)

#__________________________________________________________________________________________
## 1. # load one line to memory at a time; slow, but not loading a big file into memory
fname = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\file_rd_wr.py"

lines = []
with open(fname) as fin:
    for line in fin: #  read line by line
        # each line is a string, ended with "\n"
        # to remove "\n"
        # line = line.rstrip('\n')
        lines.append(line)

print(lines)

# each line includes "\n"
# ['from shutil import copyfile, copy2 # copytree\n', 'import os\n', 'import shutil\n', '\n', '# with open(file, "r") as fin:\n',

## 2. readlines() vs readlines(num_of_chars)
fname = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\file_rw.py"
#
with open(fname) as fin:
    # readlines() load the whole file into memory, and return a list of strings (lines)
    # readlines(n): n: # of chars; read a list of lines up to a total of n chars
    lines = fin.readlines()

print(lines)
# ['from shutil import copyfile, copy2 # copytree\n', 'import os\n', 'import shutil\n', '\n', '# with open(file, "r") as fin:\n',

fname = "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\file_rw.py"

res = []
with open(fname, 'r', encoding='utf-8') as fin:
    num_chars = 100
    rest = fin.readlines(num_chars)
    # read in lines upto num_chars

    print(rest)
# ['from shutil import copyfile, copy2 # copytree\n', 'import os\n', 'import shutil\n', '\n', '# with open(file, "r") as fin:\n']fname = "C:\\Users\jsun\Documents\Desk_2\Py_op\File_op\\file_rw.py"
#
res = []
with open(fname, 'r', encoding='utf-8') as fin:
    num_chars = 100
    rest = fin.readlines(num_chars)
    # read in lines upto num_chars

    print(rest)
# # ['from shutil import copyfile, copy2 # copytree\n', 'import os\n', 'import shutil\n', '\n', '# with open(file, "r") as fin:\n']

## 3.
def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f = open('bigFile')
for chuck in readInChunks(f):
    do_something(chunk)
f.close()

## 4. writelines(): write a list of lines at one time
#___________________________________________________________________________
res = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\outfile.txt"
with open(res, "w") as output:
    lines =[]
    in_file =  "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_test.txt"

    with open(in_file, "r") as input:
        for line in input:
            lines.append(line)
            if len(lines) == 5:
                output.writelines(lines)
                #writelines(list_of_strings): write a list of strings to file
                lines.clear()
        output.writelines(lines)

    output.writelines([])

#___________________________________________________________________________
## 5.
# write(string): write a string as a line to a file.
# write(arg) expects a string as argument and writes it to the file.
# If you provide a list of strings, it will raise an exception (btw, show errors to us!).
res = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\outfile1.txt"
in_file =  "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\logging_test.txt"
with open(res,"w") as output:
    with open(in_file,"r") as input:
        for line in input:
            output.write(line)


#_______________________________________________________________________________
#_______________________________________________________________________________
## 6.
#with open(source, 'r') as src, open(dest, 'w') as dst: dst.write(src.read())
#f.read() reads the file as an individual string, and so allows relatively easy
# file-wide manipulations, such as a file-wide regex search or substitution.

#f.readline() reads a single line of the file


newfile = r"newfile.txt"
with open(newfile, "r") as input:
    with open(newfile, "w") as output:
        a = input.readlines()
        # readlines(): read the whole file into a list of strings, each line corresponds to one line.
        # read(): read the  the whole file into a single string.

        # writelines(list_of_string): write a list of strings to a file
        # write(string): write a single string to a file.
        print(a)
        output.writelines(a)

#___________________________________________________________________________
#___________________________________________________________________________
# 7. ("a") mode
infile = r"outfile.txt"
append_file = r"outfile_2_17_21_2.txt.txt"

# in 'append' mode, if file doesn't exist, it will create one just like file write
with open(append_file,'a') as output:
    with open(infile, 'r') as input:
        for line in input:
            output.write(line)
        output.writelines(['\n','\n','End of the first write\n'])

with open(append_file,'a') as output:
    with open(infile, 'r') as input:
        for line in input:
            output.write(line)
#
# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - ERROR- An err.
#
#
# End of the first write
# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - ERROR- An err.
#___________________________________________________________________________

##8. "w+" write and then read
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\outfile3.txt"
test_item = "This is a test\n"
test_list = ["FW test\n", "API test\n", "UI test\n"]

with open(file_name,"w+") as fw:
    fw.write(test_item)
    fw.writelines(test_list)

    fw.seek(16)

    print(f"current cursor is at {fw.tell()}")
    line = fw.read()
    print(f"text after cursor is \n {line}")
    print(fw.tell())

# current cursor is at 16
# text after cursor is
#  FW test
# API test
# UI test
#
# 44

## 8.1 write and read: "w+"
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\outfile3.txt"
test_item = "This is a test\n"
test_list = ["FW test\n", "API test\n", "UI test\n"]

with open(file_name,"w+") as fw:
    fw.write(test_item)
    fw.writelines(test_list)

    fw.seek(0)
    for line in fw:
        print(line.rstrip("\n"))

# This is a test
# FW test
# API test
# UI test

## 8.2 read and write "r+"
with open("relayTest.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "OldPath"
    data["location_mod"] = "Path_NEW"
    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=4, sort_keys=True)
    jsonFile.truncate() # in case, new data file size is smaller

## 8.3 "rb" read in binary
with open(file_name, "w+") as fw:
    fw.write(test_item)
    fw.writelines(test_list)

    fw.seek(0)
    for line in fw:
        print(line.rstrip("\n"))

with open(file_name, "rb") as f:
    for line in f:
        print(line)

# This is a test
# FW test
# API test
# UI test
# b'This is a test\r\n'
# b'FW test\r\n'
# b'API test\r\n'
# b'UI test\r\n'

## 20 samples
## 20.1
file_name = "fun1.py"
with open(file_name) as f:
    #lines: a list of strings, each string representing a line
    lines = f.readlines()
for line in lines:
    print(line,end="")
    # use rstrip to remove "\n"
    print(line.rstrip("\n"))
# without "\n"
#f.read().splitlines()

## 20.2
def readline():
    with open("sorted_output.txt") as f:
        # line is a single string, ended with "\n"
        line = f.readline()
        lines = []
        while line:
            lines.append(line)
            line = f.readline()
##20.3
import os.path
import zipfile

with zipfile.ZipFile('log_all.zip',"w") as zf:
    file_list = ['Run_QA.py','doc_dir.txt','Run_Pkg_Installation_test.py']
    for item in file_list:
        zf.write(item)

with zipfile.ZipFile('log_all.zip','r') as zf:
    unzip_folder = 'unzipped_content'
    zf.extractall(unzip_folder)
    zipped_files = os.listdir(unzip_folder)
    print(zipped_files)