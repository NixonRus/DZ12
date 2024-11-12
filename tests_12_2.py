import runner_and_tournament as runner
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = runner.Runner('Усэйн', 10)
        self.Andre = runner.Runner('Андрей', 9)
        self.Nick = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print(i, '\n')

    def test_tournament_1(self):
        self.Tournament = runner.Tournament(90, self.Usain, self.Nick)
        self.all_results[1] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][2] == 'Ник')

    def test_tournament_2(self):
        self.Tournament = runner.Tournament(90, self.Andre, self.Nick)
        self.all_results[2] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][2] == 'Ник')

    def test_tournament_3(self):
        self.Tournament = runner.Tournament(90, self.Usain, self.Andre, self.Nick)
        self.all_results[3] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][3] == 'Ник')

    def test_tournament_4(self):
        self.Tournament = runner.Tournament(6, self.Usain, self.Andre, self.Nick)
        self.all_results[4] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
