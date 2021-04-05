fname = 'outfile.txt'

res = []
with open(fname, 'r') as fin:
    for line in fin:
        # It does include line-breaker "\n"
        res.append(line)

print(res)
# ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n', '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']


with open(fname, 'r') as fin:
    res = fin.readlines()
    # include line-breaker "\n"

print(res)
# ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n', '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']

res = []
with open(fname, 'r') as fin:
    for line in fin:
        res.append(line.strip('\n'))
print(res)
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log', '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']

with open(fname, 'r') as fin:
    result = fin.read()
    # include line-breaker "\n"
    re1 = result.splitlines()
    re2 = result.split("\n")
print(re1)
print(re2)
print(re2[0:-1])
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log', '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log', '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.', '']
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log', '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']