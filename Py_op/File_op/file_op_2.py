"""
os.path.split()
os.path.isfile()
os.path.abspath()
os.path.split(Filename)
os.path.splitext(filename)[0]
os.listdir
"""

"""
os.path.abspath returns the absolute path, but does NOT resolve symlinks.
os.path.realpath will first resolve any symbolic links in the path, and then return the absolute path.
"""


##1.

def recursive_copy_files(source_path, destination_path, override=False):

    files_count = 0
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    items = glob.glob(source_path + '/*')
    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination_path, item.split('/')[-1])
            files_count += recursive_copy_files(source_path=item, destination_path=path, override=override)
        else:
            file = os.path.join(destination_path, item.split('/')[-1])
            if not os.path.exists(file) or override:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count
##2.

filename = "b_file_op2.py"
file_path = os.path.abspath(filename) # give full path :  'C:\\Users\\jsun\\Documents\\PyProj\\file_op\\b_file_op2.py'
path_list = os.path.split(file_path)

print(type(path_list)) #<class 'tuple'>
print(path_list) #('C:\\Users\\jsun\\Documents\\PyProj\\file_op', 'b_file_op2.py')

file_path = path_list[0]
path_list = os.path.split(file_path)
print(path_list) # ('C:\\Users\\jsun\\Documents\\PyProj', 'file_op')

## 3.
from glob import glob
import os
from datetime import datetime
schfile = os.path.join(os.getcwd(),"**","*.txt")
#a = glob(schfile, recursive=True)
#for i in a:
 #   print(i)


## 4.
a = os.stat("file_test.py")
print(os.stat("file_test.py"))
print(type(os.stat("file_test.py")))

print("size is {} bytes".format(a.st_size))
print("atime is {}".format(datetime.fromtimestamp(a.st_atime).strftime("%Y_%m_%d_%H_%M_%S")))
print("mtime is {}".format(datetime.fromtimestamp(a.st_mtime).strftime("%Y_%m_%d_%H_%M_%S")))
print("ctime is {}".format(datetime.fromtimestamp(a.st_ctime).strftime("%Y_%m_%d_%H_%M_%S")))

## 5.

##
cur_dir = os.getcwd()
ss = os.path.basename(cur_dir)
print(cur_dir) # C:\Users\jsun\Documents\Desk_1
print(ss)      # Desk_1

src_filename = os.path.abspath("__file__")
print(src_filename) # C:\Users\jsun\Documents\Desk_1\__file__

##
# temp = ""
# for (root, dir, file) in os.walk(os.getcwd(), topdown = True):
#     print("root   ->{}".format(root))
#     print("dir    -> {}".format(dir))
#     print("file   -> {}".format(file))
#     print("root dirname  is {}".format(os.path.dirname(root)))
#     print("root basename is {}".format(os.path.basename(root)))
#     if root != temp:
#         temp = root
#         print("---------------------------------------------------------")
#
#

##
# #os.path.split(path) split the pathname path into a pair; (head, tail).
#
# #os.path.dirname(path) returns the head of the path.
# #The dirname of '/foo/bar/item' is '/foo/bar'.
#
# #os.path.basename(path) returns the tail of the path.
# # The basename of '/foo/bar/item' returns 'item'
#
# for i in os.listdir("."):
#     print(i, os.path.basename(os.path.abspath(i)), os.path.dirname(os.path.abspath(i)), sep=", ")
#
# # find file size
#
# def getFilesize(file):
#     with open(file,"r") as f:
#         f.seek(0, os.SEEK_END)# os.SEEK_SET, os.SEEK_CUR
#         #fstream = open(file, 'r')
#         #fstream.seek(0, os.SEEK_END)
#         FILE_SIZE = f.tell()
#         return FILE_SIZE
#
# if __name__  == "__main__":
#     import os
#     print("file size is ", os.path.getsize(__file__))
#     print("file size is ", os.stat(__file__).st_size)
#     print(getFilesize(__file__))
# #rename directory
# import os
#
# for dirs in os.listdir(os.getcwd()):
#     if os.path.isdir(dirs):
#         dirs_replace = dirs.replace("Chapter", "result_log")
#         print(dirs_replace)
#         os.rename(dirs, dirs_replace)
#
# #

## 6.
import os
file_name, file_ext = os.path.splitext("script.txt")
print(file_name)
print(file_ext)
# script
# .txt

## 7.
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\outfile3.txt"
print(os.path.basename(file_name)) # outfile3.txt
print(os.path.dirname(file_name)) # C:\Users\jsun\Documents\Desk_1\Py_op\File_op

res_tuple = os.path.split(file_name) # type is tuple
print(res_tuple[0])# C:\Users\jsun\Documents\Desk_1\Py_op\File_op
print(res_tuple[1]) # outfile3.txt

file_tuple = os.path.splitext(res_tuple[1])
print(file_tuple[0]) # outfile3
print(file_tuple[1]) # .txt

## 8.

d = os.path.exists('\\c:\\home\\foo\\bar\\')
print(d)  # False
print(type(d))  # <class 'bool'>
#
d = os.path.isfile('C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\fun1.py')
print(d)  # True
print(type(d))  # <class 'bool'>
#
d = os.path.isdir('C:\\Users\\jsun\\Documents\\pyProjects')
print(d)  # True
print(type(d))  # <class 'bool'>
