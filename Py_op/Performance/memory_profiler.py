import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    load_json('allthethings.json')


# $ python -m memory_profiler json_demo.py
# Filename: json_demo.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      3   13.430 MiB    0.000 MiB   @profile
#      4                             def load_json(filename):
#      5   13.434 MiB    0.004 MiB       with open(filename, 'r') as f:
#      6   86.773 MiB   73.340 MiB           return json.load(f)


$ time python ijson_demo.py

real    0m2.966s
user    0m2.944s
sys    0m0.020s