import unittest
"""
class MyUnitTest(unittest.TestCase):

    def setup(self):
        print("In setup.. ")

    def tearDown(self):
        print("Tearing down the test")
        print("~"*10)

    def test_2(self):
        print("In test 2")
        self.assertEqual(1+2, 6)

    def test_1(self):
        print("in test 1")
        self.assertTrue( 1+ 2 == 3)

    @unittest.skip("Skipping test_3")
    def test_3(self):
        print("Not used")

#if __name__ == "__main__":
    #unittest.main()
"""
def get_num():
    s = input("input number (Enter to quit): ")
    if not s:
        return None
    else:
        return float(s)

print(get_num())
