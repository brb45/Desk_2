import time
import threading
from multiprocessing import Queue

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._queue.get()
            # Checks if the current message is
            # the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print("I'm a thread, and I received %s!!" % msg)

        # Always be friendly!
        print('Bye byes!')

def Producer():
    # Queue is used to share items between
    # the threads.
    queue = Queue()

    # Create an instance of the worker
    worker = Consumer(queue)
    # start calls the internal run() method to
    # kick off the thread
    worker.start()

    # variable to keep track of when we started
    start_time = time.time()
    # While under 5 seconds..
    while time.time() - start_time < 5:
        # "Produce" a piece of work and stick it in
        # the queue for the Consumer to process
        queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)

    # This the "poison pill" method of killing a thread.
    queue.put('quit')
    # wait for the thread to close down

    worker.join()
    print("done")


if __name__ == '__main__':
    Producer()

# "C:\Users\jsun\My Documents\venv\Scripts\python.exe" C:/Users/jsun/Documents/Py_projects/mul_process/mul_process_old_log15.py
# I'm a thread, and I received something at 1558290587.0497932!!
# I'm a thread, and I received something at 1558290588.0517473!!
# I'm a thread, and I received something at 1558290589.052209!!
# I'm a thread, and I received something at 1558290590.0522926!!
# I'm a thread, and I received something at 1558290591.0525973!!
# Bye byes!
# done