import random

import calc
import unittest

class CalcTest(unittest.TestCase):
    def setUp(self):
        """
        функция, запускающаяся перед каждым тестом
        :return:
        """
        print('setup')

    @classmethod
    def setUpClass(cls):
        """
        запускается в самом начале и 1 раз
        :return:
        """
        print('megaSetup')

    def tearDown(self):
        """
        после каждого теста
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        в конце
        :return:
        """
        pass

    @unittest.skip('для теста')
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 2), 'на везение')
    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)


if __name__ == "__main__":
    unittest.main()

"""def test_add():
    if calc.add(1, 2) == 3:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) is fail')

test_add()"""