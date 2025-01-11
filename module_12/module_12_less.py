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

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_test(self):
        # self.assert...
        pass


if __name__ == "__main__":
    unittest.main()

"""def test_add():
    if calc.add(1, 2) == 3:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) is fail')

test_add()"""