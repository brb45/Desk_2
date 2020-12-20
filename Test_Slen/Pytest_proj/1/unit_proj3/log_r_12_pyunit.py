if __name__ == "__main__":
    import unittest
    from log_r_12 import *
    suite = unittest.TestLoader().loadTestsFromTestCase(\
                                        ShoppingCartTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
