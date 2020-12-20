# Replace lines without changing file permission

# method 1
# Reading the file as a single string
# Make changes to the string
# overwrite the file with the new string
import re
def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()

# method 2
# write to a different file line by line
# if no changes, write the same line or change the line and write back
file_rd =  "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\newfile.txt"
file_wt = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\newfile_change.txt"
# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - ERROR- An err.

with open(file_rd) as fin:
    with open(file_wt, "w") as fout:
        for line in fin:
            line = line.replace('ERROR', 'TO_BE_ERROR')
            fout.write(line)


# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - TO_BE_ERROR- An err.


###########

## NOT working
from tempfile import mkstemp
from shutil import move
import os
import sys

def replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                target_file.write(line.replace(pattern, substring))
    os.remove(source_file_path)
    move(target_file_path, source_file_path)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        replace(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print ("""Invalid command 
        Usage: python replacelinesinfile.py [source_file_path] [pattern] [substring]
        """)


