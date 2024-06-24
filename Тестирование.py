import unittest

class Student:
    def __init__(self):
        self.distance = 0

    def walk(self):
        self.distance += 50

    def run(self):
        self.distance += 100

class TestStudent(unittest.TestCase):
    def test_walk(self):
        student = Student()
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, f"Дистанции не равны {student.distance} != 500")

    def test_run(self):
        student = Student()
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, f"Дистанции не равны {student.distance} != 1000")

    def test_competition(self):
        running_student = Student()
        walking_student = Student()
        for _ in range(10):
            running_student.run()
            walking_student.walk()
        self.assertGreater(running_student.distance, walking_student.distance, f"{running_student.distance} должен преодолеть дистанцию больше чем {walking_student.distance}")

if __name__ == '__main__':
    unittest.main()