import unittest
import module_12_less

calcTS = unittest.TestSuite()
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_less.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)