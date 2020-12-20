import subprocess
import time
# Use subprocess

##1
cmd = ['ping', '127.0.0.1', '-n', '5']
# exec = subprocess.Popen(cmd) # start executing
# time.sleep(10)
# exec.wait() # wait until exec is done executing.
print("done")

##2
# exec = subprocess.Popen(cmd, stdout=subprocess.PIPE)
# exec.wait()
# print("done")
# # for line in exec.stdout:
# #     print(line.decode('utf-8').strip())
# #     print(line)

##3
# p1 = subprocess.Popen('dir', shell=True)
# p1.wait()


##4,
# p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)
# p1.stdout.close()
# out, err = p2.communicate()

# ##
print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'], shell=True,
    stdout=subprocess.PIPE
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

