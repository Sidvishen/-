import unittest
from TestCase import Runner
import logging

logging.basicConfig(filename='../../runner_tests.log', level=logging.INFO, filemode='w', format='%(levelname)s: %(message)s',
                    encoding='utf-8')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("John", -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

if __name__ == '__main__':
    unittest.main()