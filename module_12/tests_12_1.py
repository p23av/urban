import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        same = Runner('Walk')
        for i in range(10):
            same.walk()
        self.assertEqual(same.distance, 50)

    def test_run(self):
        same = Runner('Run')
        for i in range(10):
            same.run()
        self.assertEqual(same.distance, 100)

    def test_challenge(self):
        runner_1 = Runner('Chal')
        runner_2 = Runner('Lenge')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

RunnerTest()