# ch4/example1.py
import os, shutil
n_files = 10
files = []

# method 1
file_dir = "output2"
if os.path.isdir(file_dir):
    shutil.rmtree(file_dir)
os.mkdir(file_dir)
file_descriptor = []
for i in range(n_files):
    file = os.path.join(file_dir, "logall{}.txt".format(i))
    t= open(file, 'w')
    file_descriptor.append(t)

line = 0
for i in file_descriptor:
    print(line, i, sep="-")
    line += 1

# method 2
'''for i in range(n_files):
    f = open('output1/sample%i.txt' % i, 'w')
    files.append(f)
    f.close()'''

# method 3
'''for i in range(n_files):
    with open('output1/sample%i.txt' % i, 'w') as f:
        files.append(f)'''
