fname = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\file_rd_wr.py"

lines = []
with open(fname) as fin:
    for line in fin:
        # each line is a string, ended with "\n"
        # to remove "\n"
        # line = line.rstrip('\n')
        lines.append(line)

print(lines)


with open(fname, 'r') as fin:
    for line in fin:
        lines.append(line)

with open(fname) as fin:
    # readlines() load the whole file into memory, and return a list of strings (lines)
    # readlines(n): n: # of chars; read a list of lines up to a total of n chars
    lines = fin.readlines()

print(lines)

with open(fname, 'r') as fin:
    lines = fin.readlines()

with open(fname, 'r', encoding='utf-8') as fin:
    liens = fin.readlines()