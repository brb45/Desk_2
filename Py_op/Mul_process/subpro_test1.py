import time
import subprocess

test_cmd = "".join([
    "import time;",
    "print('starting script{}...');",
    "time.sleep(1);",
    "print('script{} done.')"
])

for i in range(2):
    subprocess.Popen(
        # ["python", "-c", test_cmd.format(*[i, i])], shell=True).wait()
        ["python", '-c', test_cmd.format(i,i)], shell=True).wait()
    print('-'*80)
print(test_cmd)

test_cmd = ["python", "basic_test.py"]
run_proc = subprocess.Popen(test_cmd)
#run_proc.wait()
print("done")
time.sleep(3)