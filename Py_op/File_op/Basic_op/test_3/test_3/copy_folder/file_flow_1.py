import errno
import os
filepath = "C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op/test_1"
log_file = os.path.join(filepath,"doc_dir.txt")
try:
    with open(log_file,"w") as my_file:
        my_file.write("start of test")
except IOError as error:
    if error.errno == errno.ENOENT:
        print ('ignoring error because directory or file is not there')
    else:
        print("error to open\n")

#open to write
if not os.path.exists(filepath):
    try:
        os.makedirs(filepath)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
with open(log_file, 'a') as my_file:
    my_file.write("Start of the test\n")

#
import os.path
path = os.path.join("C:\\Users\\jsun\\Documents\\Desk_1\\Py_op\\File_op\\Basic_op\\test_1","QA_Auto.txt")

file_dir = os.path.split(path)
# print(type(file_dir))
# <class 'tuple'>
print(file_dir) #
# ('C:\\Users\\jsun\\Documents\\Desk_1\\Py_op\\File_op\\Basic_op\\test_1', 'QA_Auto.py')

file_name = os.path.splitext(file_dir[-1])
# print(type(file_name), file_name, "\n")
# <class 'tuple'> ('QA_Auto', '.py')

ls_dir = os.listdir("C:\\Users\\jsun\\Documents\\Desk_1\\Py_op\\File_op")
print(ls_dir) # ['test_1']
dir_name = os.path.dirname(path)
is_dir = os.path.isdir(dir_name)
print(is_dir, "\n") # True

try:
    with open(path, "w") as fout:
        file_list =[]
        [file_list.append(f) for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
        #fout.writelines(file_list)
        for item in file_list:
            fout.write(item+"\n")
except IOError:
    print("An I/O error has occurred!")
except:
    print("An unknown error has occurred!")
finally:
    print("file write done")

