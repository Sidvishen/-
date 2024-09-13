import unittest

class RunnerTest(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    def test_tournament(self):
        self.assertEqual(1, 1)

class RunnerTest(unittest.TestCase):is_frozen = False
def run_if_not_frozen(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_frozen:
            return func(self, *args, **kwargs)
        else:
            print('Тесты в этом кейсе заморожены')
    return wrapper

class TournamentTest(unittest.TestCase):is_frozen = True
def run_if_not_frozen(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_frozen:
            return func(self, *args, **kwargs)
        else:
            print('Тесты в этом кейсе заморожены')
    return wrapper




