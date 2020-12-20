#celery_test2.py
#mergeSort.py
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

##########################################################################################
# main.py
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

#############################################################################
# HOST3 $ celery -A mergesort worker --loglevel=info

# HOST4 $ python3.5 main.py
# Distributed mergesort took 10.84s
# Local mergesort took 26.18s