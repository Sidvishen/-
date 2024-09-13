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

    def __repr__(self):
        return self.name

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
        cls.all_variants = []

    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_variants):
            print(f'{i + 1}. {elem}')

if __name__ == '__main__':
    unittest.main()