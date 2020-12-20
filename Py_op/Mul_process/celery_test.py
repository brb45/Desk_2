#test.py created on HOST3
import celery

app = celery.Celery('test',
                        broker='amqp://HOST1',
                        backend='amqp://HOST1') # use RabbitMQ as result backend

                        #backend='redis://HOST2')


@app.task
def echo(message):
    return message


HOST1 $ sudo /usr/local/sbin/rabbitmq-server
HOST2 $ sudo /usr/local/bin/redis-server

# HOST3 $ celery -A test worker --loglevel=info
# Start a pool of remote workers on terminal HOST3
# HOST4:
#running from HOST4 (master process, client)
from test import echo
>>> res = echo('Python rocks!')
>>> print(res)
Python rocks!

# Running on HOST3 (master process)
>>> res = echo.delay('Python rocks!'); print(type(res)); print(res)
<class 'celery.result.AsyncResult'>
1423ec2b-b6c7-4c16-8769-e62e09c1fced
>>> res.ready()
True
>>> res.result
'Python rocks!'

