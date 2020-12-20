import concurrent.futures
import urllib.request

URLS = ['http://www.baidu.com/',
        'http://www.sina.com/',
        'http://www.mi.com/',
        'http://jd.com/',
        'http://taobao.com/']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    print(type(future_to_url))
    print("future_to_url is {}".format(future_to_url))
for future in concurrent.futures.as_completed(future_to_url):
    url = future_to_url[future]
    try:
        data = future.result()
    except Exception as exc:
        print('%r generated an exception: %s' % (url, exc))
    else:
        print('%r page is %d bytes' % (url, len(data)))

