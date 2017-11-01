from unittest import TestCase
import mean as m


class TestMean(TestCase):
    def test_sum(self):
        self.assertEqual(m.sum([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(m.sum([1, 2]), 3)

    def test_mean(self):
        self.assertEqual(m.mean([1, 2]), 1.5)
        self.assertEqual(m.mean([1, 2, 3, 4]), 2.5)

    def test_median(self):
        self.assertEqual(m.median([1, 1, 2, 3, 4]), 2)
        self.assertEqual(m.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(m.median([1, 1, 2, 3, 4, 4]), 2.5)
        self.assertEqual(m.median([1, 1, 2, 3, 4, 4, 5, 6]), 3.5)
        self.assertEqual(m.median([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(m.median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
        self.assertEqual(m.median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 6)
        self.assertEqual(m.median([50, 80, 100, 300, 9, 25, 30, 120, 550, 232]), 90.0)
        self.assertEqual(m.median([50, 80, 100, 300, 9, 25, 30, 120, 550, 232,190]), 100.0)
