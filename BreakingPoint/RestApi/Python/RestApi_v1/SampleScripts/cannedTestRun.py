import sys

sys.path.insert(0, '../Modules')
from BpsRestApi import *

# Demo 1 Script. This script will perform the following steps:
# 1. Login
# 2. Show current port reservation state and then reserve the ports
# 3. Run a canned test - 'AppSim'
#   3.a Show progress and test statistics
#   3.b After test completion, show the test result (Pass/Fail)
# 5. Unreserve the ports
# 6. Logout

bps = BPS('10.36.18.45', 'admin', 'admin')
# login
bps.login()
# showing current port reservation state
bps.portsState()
# reserving the ports.
bps.reservePorts(slot = 1, portList = [0,1], group = 1, force = True)
# running the canned test 'DDoS Ping Flood Attack' using group 1
# please note the runid generated. It will be used for many more functionalities
runid = bps.runTest(modelname = 'AppSim', group = 1)
# showing progress and current statistics
progress = 0
while (progress < 100):
    progress = bps.getRTS(runid)
    time.sleep(1)
# showing the test result (Pass/Fail)
# a sleep is put here because we do not immediately get the test results.
# inserting a sleep to allow for the data to be stored in the database before retrieval
time.sleep(1)
bps.getTestResult(runid)

# unreserving the ports.
bps.unreservePorts(slot = 1, portList = [0,1], enableRequestPrints = False)

# logging out
bps.logout()
