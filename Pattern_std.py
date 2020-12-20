from pprint import pprint
from collections import Counter
import time
import time

# infrastructure automation tools like Chef, Puppet, Ansible, SaltStack or Windows PowerShell DSC.
# Git : Version Control System tool
# Jenkins : Continuous Integration tool
# Selenium : Continuous Testing tool
# Puppet, Chef, Ansible : Configuration Management and Deployment tools
# Nagios : Continuous Monitoring tool
# Docker : Containerization tool



# _________________________________________
# [1]. Dictionary look up :
# 1) Two Sum

#_____________________________________________
# [2]. Double Pointer
# 11) Container with Most water
# 15) 3Sum (sorted)
# 16) 3Sum Closest (sorted)
# 80) Remove Duplicates from Sorted Array II

#_____________________________________________
# [3]. Pure Implementation Check
# skills of scanning the whole array
# master of for and while loop
# 31) Next Permutation
# 56) Merge Intervals
# 73. Set Matrix Zeroes
# 153. Find Minimum in Rotated Sorted Array
# 775. Global and Local Inversions
#_____________________________________________
# [4].Binary Search :sorted  array
# 33. Search in Rotated Sorted Array
# 34. Find First and Last Position of Element in Sorted Array
# 153. Find Minimum in Rotated Sorted Array
# __________________________________________
# [5]. DFS
# 39. Combinational Sum
# 40. Combinational Sum II
# 74. Search a 2D Matrix
# 78. Subsets
# 90) subset II
# 79 word search

#_____________________________________________
# [6]. Matrix rotation
# 48. Rotate Image

#_____________________________________________
# [7]. dp
#_62. Unique Path_____
# 63. Unique Path II
# 64. Minimum Path Sum, check yang
#
# _______________________________________
# [8]. Greedy
# 769. Max Chunks To Make Sorted

#___________________________________________
[10]. Parenthesis
# 20. Valid Parentheses
# 32. Longest Valid Parentheses
# 921. Minimum Add to Make Parentheses Valid
# 1190. Reverse Substrings Between Each Pair of Parentheses
# 856. Score of Parentheses
# 1249. Minimum Remove to Make Valid Parentheses

#___________________________________________
[11]. Palindrom
# 267. Palindrome Permutation II
# 1177. Can Make Palindrome from Substring

#_______________________________
# ____________
# [12]. Linked List
# 86. Partition List


def run_flow1(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode

def run_flow2(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode
from collections import deque, Counter
from pprint import pprint



def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode

def copy_setup_file(run_dir, setupfile_loc):
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)


def copy_flows(run_dir, flow_to_test, flowfile_loc ):
    for flow_name in os.listdir(flowfile_loc):
        #flow_name = os.path.split(flow_name)[-1]
        flow_name  = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)

