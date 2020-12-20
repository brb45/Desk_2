import subprocess
import time

#time.sleep(15)
cmd = "ping 127.0.0.1 -n 10"
exec = subprocess.Popen(cmd, stdout=subprocess.PIPE)
exec.wait()
print("done")
for line in exec.stdout:
    print(line.decode('utf-8').strip())
    print(line)

#time.sleep(15)