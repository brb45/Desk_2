import multiprocessing as mp
def job(x):
    return x*x
def multicore():
    pool = mp.Pool(processes=4)
    res = pool.map(job, range(10))# map returns results
    print("res is {}".format(res))
def multicore_2():
    pool = mp.Pool(processes = 4)
    res = pool.apply_async(job,(2,))
    print(res.get())

    mul_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in mul_res])

if __name__ == '__main__':
    multicore()
    multicore_2()

# res is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 4
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]