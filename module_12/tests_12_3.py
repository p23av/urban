import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            same = Runner('Walk', -30)
            for i in range(10):
                same.walk()
            self.assertEqual(same.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        same = Runner('Run')
        for i in range(10):
            same.run()
        self.assertEqual(same.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Chal')
        runner_2 = Runner('Lenge')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        self.__class__.all_results['test_1'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_1'][max(self.__class__.all_results['test_1'].keys())].name == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament_1 = Tournament(90, self.runner_2, self.runner_3)
        self.__class__.all_results['test_2'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_2'][max(self.__class__.all_results['test_2'].keys())].name == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.__class__.all_results['test_3'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_3'][max(self.__class__.all_results['test_3'].keys())].name == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.keys():
            print({place: str(runner) for place, runner in cls.all_results[result].items()})
