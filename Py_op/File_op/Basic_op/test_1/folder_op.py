import os

# __file__ = C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op/test_1/folder_op.py

file_folder_name = os.path.dirname(__file__)
# print(file_folder_name)
# C:/Users/jsun/Documents/Desk_1/Py_op/File_op/Basic_op/test_1

abs_file_folder_path = os.path.abspath(file_folder_name)
print(abs_file_folder_path)
# C:\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op\test_1

file_path = os.path.abspath(__file__)
print(file_path) # C:\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op\test_1\folder_op.py
print(type(file_path)) # <class 'str'>

file_dir, file_name = file_path.rsplit('\\', maxsplit=1)
print(file_dir) # C:\Users\jsun\Documents\Desk_1\Py_op\File_op\Basic_op\test_1
print(file_name) #  folder_op.py

path_to_join = [file_dir, '..\\', 'a', 'b', '1','2']
# dir_final = os.path.join(path_to_join)
# print(dir_final)

dir_final = os.path.join(path_to_join, 'test', 'test_ex.txt')
print(dir_final)
