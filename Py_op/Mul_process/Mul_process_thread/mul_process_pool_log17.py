
import multiprocessing
from time import sleep
import time

#work function
def calculate(process_name, tasks, results):
    print("{} evaluation routine starts".format(process_name))
    while True:
        new_value = tasks.get()
        if new_value < 0:
            print("{} evaluation routine quits".format(process_name))
            results.put(-1)
            break
        else:
            compute = new_value * new_value
            sleep(0.02 * new_value)

            print("{} received value: {}".format(process_name, new_value))
            print("{} calculated value: {}".format(process_name, compute))
            results.put(compute)
    return

if __name__ == "__main__":
    manager = multiprocessing.Manager()

    tasks = manager.Queue()
    results = manager.Queue()

    num_processes = 1
    pool = multiprocessing.Pool(processes=num_processes)
    processes = []
    start = time.clock()
    for i in range(num_processes):
        process_name = "P{}".format(i)
        new_process = multiprocessing.Process(target=calculate, args=(process_name, tasks, results))
        processes.append(new_process)
        new_process.start()
    task_list = [43, 1, 780, 256, 142, 68, 183, 334, 325, 3]
    for single_task in task_list:
        tasks.put(single_task)
    sleep(5)
    for i in range(num_processes):
        tasks.put(-1)

    num_finished_processes = 0
    while True:
        new_result = results.get()
        if new_result == -1:
            num_finished_processes += 1
            if num_finished_processes == num_processes:
                print("ALL DONE")
                break
        else:
            print("Result:" + str(new_result))

    print(time.clock() - start)

###############################################################
# "C:\Users\jsun\My Documents\venv\Scripts\python.exe" C:/Users/jsun/Documents/Py_projects/mul_process/mul_process_queue_log16.py
# P0 evaluation routine starts
# P0 received value: 43
# P0 calculated value: 1849
# P0 received value: 1
# P0 calculated value: 1
# Result:1849
# Result:1
# P0 received value: 780
# P0 calculated value: 608400
# Result:608400
# P0 received value: 256
# P0 calculated value: 65536
# Result:65536
# P0 received value: 142
# P0 calculated value: 20164
# Result:20164
# P0 received value: 68
# P0 calculated value: 4624
# Result:4624
# P0 received value: 183
# P0 calculated value: 33489
# Result:33489
# P0 received value: 334
# P0 calculated value: 111556
# Result:111556
# P0 received value: 325
# P0 calculated value: 105625
# Result:105625
# P0 received value: 3
# P0 calculated value: 9
# Result:9
# P0 evaluation routine quits
# ALL DONE
# 42.790012