import unittest

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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_1(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        self.__class__.all_results['test_1'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_1'][max(self.__class__.all_results['test_1'].keys())].name == 'Ник')

    def test_2(self):
        tournament_1 = Tournament(90, self.runner_2, self.runner_3)
        self.__class__.all_results['test_2'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_2'][max(self.__class__.all_results['test_2'].keys())].name == 'Ник')

    def test_3(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.__class__.all_results['test_3'] = tournament_1.start()
        self.assertTrue(self.__class__.all_results['test_3'][max(self.__class__.all_results['test_3'].keys())].name == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.keys():
            print({place: str(runner) for place, runner in cls.all_results[result].items()})


TournamentTest()