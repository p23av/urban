import unittest
import tests_12_3


sameTS = unittest.TestSuite()
sameTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
sameTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(sameTS)
