import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

if __name__ == "__main__":
    unittest.main()

"""def test_add():
    if calc.add(1, 2) == 3:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) is fail')

test_add()"""