import unittest
from unitest_log_1 import TestCaseDemo1
from unitest_log import TestCaseDemo2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

qa_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(qa_test)
