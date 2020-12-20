import subprocess
import time
"""
time.sleep(15)
cmd = "python log_test2.py"
exec = subprocess.Popen(cmd, stdout=subprocess.PIPE)
exec.wait()
print("done")
for line in exec.stdout:
    print(line.decode('utf-8').strip())
    print(line)

time.sleep(15)
"""

import subprocess

p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout, stdout = subprocess.PIPE)

p1.stdout.close()
out, err = p2.communicate()
print("out", out)
for i in out:
    print(i.decode("utf-8"))