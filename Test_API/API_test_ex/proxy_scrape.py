import requests

url = "http://httpbin.org/ip"
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = ":"
proxies = {
       "https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
       "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
}

r = requests.get(url, proxies=proxies, verify=False)