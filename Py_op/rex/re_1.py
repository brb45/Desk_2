import re
intf_ip = 'Gi0/0/0.911            10.200.101.242   YES NVRAM  up                    up'
match = re.search('10.200.101.242', intf_ip)
#search() will return the first occurrence only of the pattern and will ignore the rest of them.
if match:
    print (match.group())

intf_ip = '''Gi0/0/0.705            10.103.17.5      YES NVRAM  up                    up      
Gi0/0/0.900            86.121.75.31  YES NVRAM  up                    up      
Gi0/0/0.911            10.200.101.242   YES NVRAM  up                    up      
Gi0/0/0.7000           unassigned      YES unset  up                    up '''
match = re.search("\d+\.\d+\.\d+\.\d+", intf_ip)

if match:
    print (match.group())

import re
log_msg = 'Dec 20 12:11:47.417: %LINK-3-UPDOWN: Interface GigabitEthernet0/0/4, changed state to down'
match = re.search("(\w+\s\d+\s\S+):\s(\S+): Interface (\S+), changed state to (\S+)", log_msg)
if match:
    print (match.groups())# \S, non-space chars

print()


show_ip_int_br_full = """
GigabitEthernet0/0/0        110.110.110.1   YES NVRAM  up                    up      
GigabitEthernet0/0/1        107.107.107.1   YES NVRAM  up                    up      
GigabitEthernet0/0/2        108.108.108.1   YES NVRAM  up                    up      
GigabitEthernet0/0/3        109.109.109.1   YES NVRAM  up                    up      
GigabitEthernet0/0/4   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/5             10.131.71.1     YES NVRAM  up                    up      
GigabitEthernet0/0/6          10.37.102.225   YES NVRAM  up                    up      
GigabitEthernet0/1/0            unassigned      YES unset  up                    up      
GigabitEthernet0/1/1           57.234.66.28   YES manual up                    up      
GigabitEthernet0/1/2           10.10.99.70   YES manual up                    up      
GigabitEthernet0/1/3           unassigned      YES manual deleted               down    
GigabitEthernet0/1/4           192.168.200.1   YES manual up                    up      
GigabitEthernet0/1/5   unassigned      YES manual down                  down    
GigabitEthernet0/1/6         10.20.20.1      YES manual down                  down    
GigabitEthernet0/2/0         10.30.40.1      YES manual down                  down    
GigabitEthernet0/2/1         57.20.20.1      YES manual down                  down    

"""
for line in show_ip_int_br_full.split("\n"):
    match = re.search("(?P<interface>\w+\d\/\d\/\d)\s+(?P<ip>\d+.\d+.\d+.\d+)", line)
    if match:
        intf_ip = match.groupdict()
        if intf_ip["ip"].startswith("57"):
            print ("Subnet is configured on " + intf_ip["interface"] + " and ip is " + intf_ip["ip"])

from pprint import pprint
show_ip_int_br_full = """
GigabitEthernet0/0/0        110.110.110.1   YES NVRAM  up                    up      
GigabitEthernet0/0/1        107.107.107.1   YES NVRAM  up                    up      
GigabitEthernet0/0/2        108.108.108.1   YES NVRAM  up                    up      
GigabitEthernet0/0/3        109.109.109.1   YES NVRAM  up                    up      
GigabitEthernet0/0/4   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/5             10.131.71.1     YES NVRAM  up                    up      
GigabitEthernet0/0/6          10.37.102.225   YES NVRAM  up                    up      
GigabitEthernet0/1/0            unassigned      YES unset  up                    up      
GigabitEthernet0/1/1           57.234.66.28   YES manual up                    up      
GigabitEthernet0/1/2           10.10.99.70   YES manual up                    up      
GigabitEthernet0/1/3           unassigned      YES manual deleted               down    
GigabitEthernet0/1/4           192.168.200.1   YES manual up                    up      
GigabitEthernet0/1/5   unassigned      YES manual down                  down    
GigabitEthernet0/1/6         10.20.20.1      YES manual down                  down    
GigabitEthernet0/2/0         10.30.40.1      YES manual down                  down    
GigabitEthernet0/2/1         57.20.20.1      YES manual down                  down    
"""

intf_ip = re.findall(r"(?P<interface>\w+\d\/\d\/\d)\s+(?P<ip>57.\d+.\d+.\d+)", show_ip_int_br_full)
pprint(intf_ip)

from netmiko import ConnectHandler
#from devices import R1, SW1, SW2, SW3, SW4
import multiprocessing as mp
from datetime import datetime

nodes = ["R1"]#, "SW1", "SW2", "SW3"]

def connect_to_dev(nodes):

    #net_connect = ConnectHandler(**device)
    #output = net_connect.send_command("show run")
    print (nodes)

processes = []

start_time = datetime.now()
for device in nodes:
    print("Adding Process to the list")
    processes.append(mp.Process(target=connect_to_dev, args=(device,)))

print("Spawning the Process")
#for p in processes:
    #p.start()

print("Joining the finished process to the main truck")
#for p in processes:
    #p.join()

end_time = datetime.now()
print("Script Execution tooks {}".format(end_time - start_time))

#
def connect_to_dev(device, mp_queue):
    #dev_id = device['ip']
    #return_data = {}
    #net_connect = ConnectHandler(**device)
    ###output = net_connect.send_command("show run")
    ##return_data[dev_id] = output
    #print("Adding the result to the multiprocess queue")
    mp_queue.put(return_data)

mp_queue = mp.Queue()
processes = []

for device in nodes:
    #p = multiprocessing.Process(target=connect_to_dev, args=[device, mp_queue])
    print("Adding Process to the list")
    #processes.append(p)
    #p.start()

for p in processes:
    print("Joining the finished process to the main truck")
    #p.join()

results = []
for p in processes:
    print("Moving the result from the queue to the results list")
    #results.append(mp_queue.get())

#pprint(results)
import subprocess
print(subprocess.Popen("ipconfig"))
print(subprocess.Popen(["ifconfig"]))
print(subprocess.Popen(["sudo", "ifconfig", "enp60s0:0", "10.10.10.2", "netmask", "255.255.255.0", "up"]))