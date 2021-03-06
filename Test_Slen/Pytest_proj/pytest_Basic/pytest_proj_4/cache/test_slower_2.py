import pytest
import datetime
import random
import time
from collections import namedtuple

Duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope='session')
def duration_cache(request):
    print("\nrequest is ", request)
    print("[duration_cache] starts")
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)
    print("[duration_cache] ends")


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    print("[check_duration] starts")
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration
    if d.last.get(nodeid, None) is not None:
        errorstring = "test duration over 2x last duration"
        assert duration <= (d.last[nodeid] * 2), errorstring

    print("[check_duration] ends")


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
