import unittest

suite_12_3 = unittest.TestSuite()
suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_12_3)