
We will implement two simple but interesting applications using Celery. The first one is a reimplementation of the currency exchange rate example from Chapter 3, Parallelism in Python, and the second one is a distributed sort algorithm.

We are going to use a total of four machines again (HOST1, HOST2, HOST3, and HOST4) for all these examples. As we did before, machine one (HOST1) will run RabbitMQ. The second machine (HOST2) will run Redis, the third one (HOST3) will run Celery workers, and finally, the fourth one (HOST4) will run our main code.

Let's start with a simple example. Create a new Python script (celery/currency.py) and write the following code (if you're not using Redis, remember to change backend to 'amqp://HOST1'):

import celery
import urllib.request


app = celery.Celery('currency',
                    broker='amqp://HOST1',
                    backend='redis://HOST2')


URL = 'http://finance.yahoo.com/d/quotes.csv?s={}=X&f=p'

@app.task
def get_rate(pair, url_tmplt=URL):
    with urllib.request.urlopen(url_tmplt.format(pair)) as res:
        body = res.read()
    return (pair, float(body.strip()))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('pairs', type=str, nargs='+')
    args = parser.parse_args()

    results = [get_rate.delay(pair) for pair in args.pairs]
    for result in results:
        pair, rate = result.get()
        print(pair, rate)
The preceding commands are almost identical to the thread version we saw in Chapter 3, Parallelism in Python. The main difference is that since we are using Celery, we do not need to create queues; Celery does that for us behind the scenes. In addition, instead of spawning one thread per currency pair, we simply let our Celery workers take care of fetching the work requests from the queue, executing the corresponding function calls, and once this is done, returning the results.

It is instructive to explore a few possible behaviors, such as a successful call, a call that is not worked on because of lack of workers, and a call that fails and raises an exception. Let's start with the straightforward case where everything works.

As we did in the simple echo application, let's start (unless they are already running) RabbitMQ and Redis on their respective host(s) (again, via the redis-server and rabbitmq-server command-line tools).

Then, on the worker host (HOST3), copy the currency.py script over, change cd to its directory, and start a pool of Celery workers (remember that by default, Celery starts as many worker processes as there are CPU cores), as shown in the following command:

HOST3 $ celery -A currency worker --loglevel=info
Finally, copy the same script over to HOST4 and run it as follows:

HOST4 $ python3.5 currency.py EURUSD CHFUSD GBPUSD GBPEUR CADUSD CADEUR
EURUSD 1.0644
CHFUSD 0.986
GBPUSD 1.5216
GBPEUR 1.4296
CADUSD 0.751
CADEUR 0.7056
Everything worked just fine and we got our five exchange rates back. If we look at the terminal where we started the worker pool (HOST3), we will see some log entries similar to the ones shown in the following screenshot:

More complex Celery applications
These are the default log entries that Celery workers emit at loglevel=info. Each task is assigned a unique ID (for example, f8658917-868c-4eb5-b744-6aff997c6dd2 for the task fetching the GBP versus USD rate), and basic timing information is printed for each of them in addition to their return values.

What would happen if there were no workers available? The simple way to find out is to stop the workers (via CTRL + C in their terminal window) and rerun currency.py on HOST4, as shown in this command:

HOST4 $ python3.5 currency.py EURUSD CHFUSD GBPUSD GBPEUR CADUSD CADEUR
Nothing happens, and currency.py hangs around waiting for some workers to come online and perform the work. This behavior might or might not be what we want; on one hand, it sure is convenient to have our script wait for workers to become available without crashing. On the other hand, we might want to give up waiting after a while. One way of doing this is to use the optional timeout argument in result.get().

For instance, modifying the code to use result.get(timeout=1) would result in the following output (still in the absence of workers):

HOST4 $ python3.5 currency.py EURUSD CHFUSD GBPUSD GBPEUR CADUSD CADEUR
 Traceback (most recent call last):
  File "currency.py", line 29, in <module>
    pair, rate = result.get(timeout=1)
  File "/venvs/book/lib/python3.5/site-packages/celery/result.py", line 169, in get
    no_ack=no_ack,
  File " /venvs/book/lib/python3.5/site-packages/celery/backends/base.py", line 226, in wait_for
    raise TimeoutError('The operation timed out.')
celery.exceptions.TimeoutError: The operation timed out.
Of course, we should always use timeouts and catch the corresponding exceptions as part of our error handling strategy.

One interesting point to keep in mind is that, by default, task queues are persistent and their entries do not expire (Celery allows us to configure things differently if we choose to). This means that, if we started some workers now, they would start fetching pending tasks from the queue and return exchange rates. We can clean the queue using the celery command-line tool as follows:

HOST4 $ celery purge
WARNING: This will remove all tasks from queue: celery.
         There is no undo for this operation!

(to skip this prompt use the -f option)

Are you sure you want to delete all tasks (yes/NO)? yes
Purged 12 messages from 1 known task queue.
Let's now see what happens if, for some reason, our tasks generate an exception. Modify the currency.py script (on HOST3 at the very least) so that get_rate throws an exception, as follows:

@app.task
def get_rate(pair, url_tmplt=URL):
    raise Exception('Booo!')
Now, restart the pool of workers on HOST3 (that is, HOST3 $ celery -A currency worker --loglevel=info), and then start the main program on HOST4 as follows:

HOST4 $ python3.5 currency.py EURUSD CHFUSD GBPUSD GBPEUR CADUSD CADEUR
Traceback (most recent call last):
  File "currency.py", line 31, in <module>
    pair, rate = result.get(timeout=1)
  File "/Users/fpierfed/Documents/venvs/book/lib/python3.5/site-packages/celery/result.py", line 175, in get
    raise meta['result']
Exception: Booo!
What just happened is that all our workers raised exceptions that got propagated to the calling code and returned to us at the first call to result.get().

We should be careful to catch any exceptions that our tasks might raise. We need to keep in mind that code that runs remotely might fail for a number of reasons not necessarily related to the code itself, and we need to be able to react gracefully in those cases.

Celery helps us in a number of ways; as we saw, we can use timeouts to fetch results. We can have failed tasks be resubmitted automatically (refer to the retry parameter in the task decorator). We can also expire requests for work (refer to the expires parameter in a task's apply_async method, which is just a more powerful variant of delay that we used so far).

Sometimes, we have more complex task graphs than we have seen so far. In these cases, the result of one or more tasks needs to be fed to another task. Celery has support for sophisticated calling patterns that, it should be noted, come with some important performance penalties.

To investigate these, let's implement our second example: a distributed merge sort algorithm. This is going to be a longer code example split into two files: one for the algorithm itself (mergesory.py) and one for the main code (main.py).

Mergesort is a simple algorithm based on the idea of recursively splitting an input list in half, sorting the two halves, and then merging the results together. Create a new Python script (celery/mergesort.py) with the following code:

import celery


app = celery.Celery('mergesort',
                        broker='amqp://HOST1',
                        backend='redis://HOST2')


@app.task
def sort(xs):
    lenxs = len(xs)
    if(lenxs <= 1):
        return(xs)

    half_lenxs = lenxs // 2
    left = xs[:half_lenxs]
    right = xs[half_lenxs:]
    return(merge(sort(left), sort(right)))


def merge(left, right):
    nleft = len(left)
    nright = len(right)

    merged = []
    i = 0
    j = 0
    while i < nleft and j < nright:
        if(left[i] < right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]
The code should be pretty straightforward; we start off by defining our Celery application object app, which uses RabbitMQ for the task queue and Redis for the result backend. Then, we define our sort algorithm, which uses the ancillary merge function to combine the two (sorted) sublists into a single sorted list.

Now, for the main code, create a second script (celery/main.py) with the following commands:

#!/usr/bin/env python3.5
import random
import time
from celery import group
from mergesort import sort, merge


# Create a list of 1,000,000 elements in random order.
sequence = list(range(1000000))
random.shuffle(sequence)

t0 = time.time()

# Split the sequence in a number of chunks and process those 
# independently.
n = 4
l = len(sequence) // n
subseqs = [sequence[i * l:(i + 1) * l] for i in range(n - 1)]
subseqs.append(sequence[(n - 1) * l:])

# Ask the Celery workers to sort each sub-sequence.
# Use a group to run the individual independent tasks as a unit of work.
partials = group(sort.s(seq) for seq in subseqs)().get()

# Merge all the individual sorted sub-lists into our final result.
result = partials[0]
for partial in partials[1:]:
    result = merge(result, partial)

dt = time.time() - t0
print('Distributed mergesort took %.02fs' % (dt))

# Do the same thing locally and compare the times.
t0 = time.time()
truth = sort(sequence)
dt = time.time() - t0
print('Local mergesort took %.02fs' % (dt))

# Final sanity checks.
assert result == truth
assert result == sorted(sequence)
As the comments in the code suggest, we first generate a suitably large sequence of integers (sequence = list(range(1000000))) in a random order (this is what random.shuffle does). Then, we split it into a small number (n=4) of sublists of approximately the same length.

Once we have the sublists, we can process them in parallel (assuming, of course, that we have more than n=4 workers available). The main trouble though is that we would like to be notified somehow when these lists have been sorted so that we can merge them back into our final sorted list.

Celery offers a number of primitives to orchestrate task execution, and group is one of them. It allows the execution of concurrent tasks by bundling them, conceptually, in a virtual task. The return value of group is GroupResult (part of the same class hierarchy as AsyncResult). The GroupResult get() method necessary in case a result backend is not available. until all the tasks in the group are done and returns their results in a list. The group callable method takes a list of task signatures (which is what you get by calling a task s() method with the arguments to the task, for example, sort.s(seq) in the preceding code). Task signatures are the mechanism that Celery uses to pass tasks as arguments to other tasks without executing them on the spot.

The rest of the code just merges the sorted sublists locally, two at a time. After the distributed sort, we then re-sort the original list locally using the same algorithm, and compare the results. At the end of the script, we compare the merge-sort results with the built-in sorted call.

To run the example, we need to start RabbitMQ and Redis if they are not running already. Then, we need to start some workers on HOST3, as follows:

HOST3 $ celery -A mergesort worker --loglevel=info
Just remember to copy mergesort.py over and to change position yourself in the same directory (or define PYTHONPATH to point out to the directory where mergesort.py lives).

After that, we can run the example on HOST4, as follows:

HOST4 $ python3.5 main.py
Distributed mergesort took 10.84s
Local mergesort took 26.18s
Looking at the Celery logs, we see the n tasks being received and worked on by the worker pool and the results being sent back to the caller.

Performance is definitely not what we were expecting. A simple implementation using multiple processes (either using multiprocessing or concurrent.futures) shows that we can expect almost n-fold performance gain with this simple algorithm (seven seconds using four workers).

The main issue here is that Celery synchronization primitives are quite expensive and should only be used when absolutely necessary. The main reason for this is that Celery keeps polling for the partial results from a group to be ready so that subsequent tasks can be scheduled. This very polling can introduce significant overheads.

back to top
Recommended Playlists  History Topics Settings Support Get the App Sign Out
© 2019 Safari. Terms of Service / Privacy Policy