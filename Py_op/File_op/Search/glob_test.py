# glob is useful in any situation where your program needs to look for a list of files
# on the filesystem with names matching a pattern.
# If you need a list of filenames that all have a certain extension,
# prefix, or any common string in the middle,
# use glob instead of writing code to scan the directory contents yourself.

# The pattern rules for glob are not regular expressions.
# Instead, they follow standard Unix path expansion rules.
# There are only a few special characters: two different wild-cards, and character ranges are supported.

import os
my_dir = os.getcwd()
my_dir = os.path.join(my_dir, "..")
 # os.chdir()
print(my_dir)

base_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\File_op\Search"
file_name = os.path.join(base_path, "search_key.txt")
search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\*\*py"

import glob
file_name = os.path.join(base_path, "glob_key.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)


file_name = os.path.join(base_path, "glob_key1.txt")
with open(file_name, "w") as fout:
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op"
    search_path=os.path.join(search_path, "Class_1/*py")
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)

file_name = os.path.join(base_path, "glob_key2.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\example_log\*"
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)


# Single Character Wildcard ?
file_name = os.path.join(base_path, "glob_key3.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\example_log\QAtest?.py"
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)

# Character Ranges
file_name = os.path.join(base_path, "glob_key4.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\example_log\*[0-9]*"
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)


# Alphabet Ranges [a-z]
file_name = os.path.join(base_path, "glob_key5.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\example_log\[a-c]*"
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)

file_name = os.path.join(base_path, "glob_key5_1.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\example_log\[b]*"
    file_list = [file+"\n" for file in glob.glob(search_path)]
    fout.writelines(file_list)

# recursive search use **/ and recursive=True
# configfiles = glob.glob('C:/Users/sam/Desktop/file1/**/*.txt', recursive=True)
# Alphabet Ranges [a-z]
file_name = os.path.join(base_path, "glob_key6.txt")
with open(file_name, "w") as fout:
    # print(glob.glob(search_path)) # return a list of strings
    search_path = "C:\\Users\\jsun\Documents\Desk_1\Py_op\**\*[0-4].py"
    file_list = [file+"\n" for file in glob.glob(search_path, recursive=True)]
    fout.writelines(file_list)