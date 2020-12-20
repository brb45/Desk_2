# currency.py
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

# HOST3 $ celery -A currency worker --loglevel=info
# Finally, copy the same script over to HOST4 and run it as follows:
#
# HOST4 $ python3.5 currency.py EURUSD CHFUSD GBPUSD GBPEUR CADUSD CADEUR
# EURUSD 1.0644
# CHFUSD 0.986
# GBPUSD 1.5216
# GBPEUR 1.4296
# CADUSD 0.751
# CADEUR 0.7056