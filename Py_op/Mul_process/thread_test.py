import threading, time

print('#1 Start of program ')


def take_pause(timer):
    time.sleep(timer)
    print("#2 timer is up for after {} seconds".format(timer))


threadObj = threading.Thread(target=take_pause,args=[3])
threadObj.start()

print("#3 End of program")
print('POWER_AVERAGE_DBM', 'DATA_RATE', 'EVM_AVG_DB', sep=' & ')
threadObj_print = threading.Thread(target=print, args=["#4",'Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj_print.start()

thread_tx = threading.Thread(target=print, args=["#5","tx1", "tx2", 'tx3'], kwargs={'sep': '::'})
thread_tx.start()

"""
#1 Start of program 
#3 End of program
POWER_AVERAGE_DBM & DATA_RATE & EVM_AVG_DB
#4 & Cats & Dogs & Frogs
#5::tx1::tx2::tx3
#2 timer is up for after 3 seconds
"""
import subprocess
#subprocess.Popen("C:\\Windows\\System32\\calc.exe")
subprocess.run("C:\\Windows\\System32\\calc.exe")

subprocess.run(["C:\Windows\System32","\calc.exe"],shell=True)