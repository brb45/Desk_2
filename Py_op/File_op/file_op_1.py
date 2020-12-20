from shutil import copy2, copy, copytree, copyfile
import os, glob
import fnmatch
import shutil

#os.path.exists will also return True if there's a regular file with that name.
#os.path.isdir will only return True if that path exists and is a directory.

# copy2 need des. folder exists
# copy2 src_file can't be dir.

# if file exists, copy2 will overwirte the file with same name.
# copy,copytree doesn't preserve meta data of copied files, copy2 does
# copy() copies the file data and the file's permission mode (see os.chmod()).
# Other metadata, like the file's creation and modification times, is not preserved.


## 1. copy a file with copy2
print(os.getcwd())
#os.remove("write_log.txt")
# os.path.join(path, *paths)
file_name = "src.txt"
src = os.path.join(os.getcwd(), file_name)
des_dir = "C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op/test_2"
des = os.path.join(des_dir, "des.txt")
shutil.copy2(src, des)
# des is a file, with a given name
shutil.copy2(src, des_dir)
# des_dir is a dir,
os.remove(des)
os.remove(os.path.join(des_dir, file_name))


## 2. copy a folder with copytree
# copytree(src_dir, des_dir)
# dec_dir can't exist; Otherwise, its an error

src_dir = "C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op/test_1"
os.chdir(des_dir)
copy_folder = "copy_folder"
# if not os.path.exists(copy_folder):
#     os.mkdir(copy_folder)
# if os.path.exists(copy_folder):
#     os.remove(copy_folder)

copytree(src_dir, copy_folder)

## 3. rmtree
# remove an existing folder with or withour content;
# if dir not present, raise an error

#By design, rmtree fails on folder containing read-only files.
#If you want the folder to be deleted regardless of whether
#it contains read-only files, then use
#shutil.rmtree('/folder_name', ignore_errors=True)

base_dir  = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op"
sub_dir = "test_2"
src_dir = os.path.join(base_dir, sub_dir)
dst_dir = os.path.join(base_dir, "test_3")
if os.path.isdir(dst_dir):
    print("dst_dir exists, and need to be rmoved")
    rmtree(dst_dir)
else: # dst_dir can't exist
    copytree(src_dir, dst_dir)
    print("dst_dir has been created!")

new_dir = os.path.join(base_dir, sub_dir, sub_dir)
# print(new_dir)
# C:\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op\test_2\test_2
new_dir = (base_dir, sub_dir, sub_dir, sub_dir)
new_dir = os.path.join(*new_dir)
# print(new_dir)
# C:\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op\test_2\test_2\test_2

ex_dir = "C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op"
print(type(os.listdir(ex_dir)))
print(os.listdir(ex_dir))
# os.listdir(folder) does NOT list subdirectories.
# <class 'list'>
# ['test_1', 'test_2']


##______________________________________________________________________________##
#os.rename(oldname, newname) # rename a file or folder

#os.remove() removes a file.
#os.rmdir() removes an empty directory.
#shutil.rmtree() deletes a directory and all its contents or an empty folder

#pathlib.Path.unlink() removes the file or symbolic link.
#pathlib.Path.rmdir() removes the empty directory

#os.makedirs("dir\dir1")
#os.mkdir("dir\dirs") # error: mkdir can't make nested directory

#os.path.abspath()
#os.path.split

## basic dir/files ops
import time, datetime
os.chdir(os.path.join(os.getcwd(), "py_network_cpy_2"))
os.chdir("..")
print(os.getcwd())
test_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(test_time)
os.mkdir(test_time)
#os.makedirs(r"rex\chi\chi\chi\buchi")
shutil.rmtree(r"rex\chi")

##
#src_files = os.listdir(src)
#for file_name in src_files:
#    full_file_name = os.path.join(src, file_name)
#    if (os.path.isfile(full_file_name)):
#        shutil.copy(full_file_name, dest)

##





