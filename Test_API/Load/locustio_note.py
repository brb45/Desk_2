#     Locust is described as an easy-to-use, distributed, user load-testing tool.
# It is intended for load-testing web sites and for figuring out how many concurrent users a system can handle.
#
# A swarm of locusts will access website. THe behavior of each locust is defined by you, and the swarming
# proocess is monitored by a web UI in real time.

    # Locust is event-driven, and it supports concurrent users on a single machine.

# pip install locustio

# Create a locustfile.py
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def get_tests(self):
        self.client.get("/tests")

    @task
    def put_tests(self):
        self.client.post("/tests",\
                         {
                             "name": "load testing",
                             "description": "Checking if a software can handle the load"
                         })

class WebsiteUser(HttpLocust):
    task_set = UserBehavior


locust --host=http://website_under_test_ip:5000

Locust webUI: http://localhost:8089
Number of users to simulate: --> number of users Our API supports
Hatch rate: # of users spawned by second
Start spawning.

From webUI:
test type: GET, POST
test Name: /tests
# of requests
# fails
Average(ms)
Min(ms)
Max(ms)
# reqs/sec

Using Charts view
Based on Max response time, we can decide how many users we can support, and # of request /s
make sure server: downtime, timeout, memory overflows

# page slow to load and show performance spikes with database calls

# Performance Test
determine the responsiveness, throughput, reliability, and scalability under a given load

Load testing:
# validate performance when subjected to workloads during production operations.

Stress Testing:
# validate performance when application under test when subjected to conditions beyond those anticipated during
# production options: # of concurrent users, or , # of requests /s

# other stressful conditions: limited memory, insufficient disk space, or server failure
# Determined to check under what conditions an application will fail, how it fails, and what indicators can be
# monitored

Baselines:
load time
# of transactions processed / s
# of web pages served / s
# resource utilization : memory usage, CPU usage

Scalability

# Scalability refers to an application’s ability to handle additional workload,
# without adversely affecting performance, by adding resources such as processor, memory,
# and storage capacity.

# Load test a web application




















































