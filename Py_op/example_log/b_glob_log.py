import glob
import os
import sys
import concurrent.futures
import timeit

"""
def make_image_thumbnail(filename):
    # The thumbnail will be named "<original_filename>_thumbnail.jpg"
    base_filename, file_extension = os.path.splitext(filename)
    return filename


# Loop through all jpeg files in the folder and make a thumbnail for each





#do some nice things...



#sys.stdout.write("Total running time: %d:%d:%d.\n" % (hours, mins, secs))

from multiprocessing import Pool


def calculate(number):
    print(number)
    return number

if __name__ == '__main__':
    pool = Pool()
    result = pool.map(calculate, range(4))
    start = timeit.default_timer()
    for i in range(1):
        for image_file in glob.glob("*.py"):
            thumbnail_file = make_image_thumbnail(image_file)
            # print(thumbnail_file)
    print(100)

    stop = timeit.default_timer()
    total_time = stop - start

    # output running time in a nice format.
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)

    from concurrent.futures import ProcessPoolExecutor
    def calculate(number):
        print(number)
    print("//")
    with ProcessPoolExecutor() as executor:
        result = executor.map(calculate, range(10,15))
    ProcessPoolExecutor().map(calculate, range(20,25))
    print("/")
"""
import concurrent.futures
import urllib.request

URLS = ['http://www.baidu.com/',
        'http://www.sina.com/',
        'http://www.mi.com/',
        'http://jd.com/',
        'http://taobao.com/',
        'http://google.com/',
        'http://yahoo.com',
        'http://usatoday.com',
        'http://nbc.com']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for line, val in enumerate(future_to_url):
        print(line, val)
for future in concurrent.futures.as_completed(future_to_url):
    url = future_to_url[future]
    try:
        data = future.result()
    except Exception as exc:
        print('%r generated an exception: %s' % (url, exc))
    else:
        print('%r page is %d bytes' % (url, len(data)))
