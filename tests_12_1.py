import Test_Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        John = Test_Runner.Runner('name1')
        for _ in range(10):
            John.walk()
        self.assertEqual(John.distance, 50)

    def test_run(self):
        Kris = Test_Runner.Runner('name2')
        for _ in range(10):
            Kris.run()
        self.assertEqual(Kris.distance, 100)

    def test_challenge(self):
        Chak = Test_Runner.Runner('name3')
        Bob = Test_Runner.Runner('name4')
        for _ in range(10):
            Chak.run()
        for _ in range(10):
            Bob.walk()
        self.assertNotEqual(Chak.distance, Bob.distance)
