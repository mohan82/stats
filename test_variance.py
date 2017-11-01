from unittest import TestCase

import stddev as s


class TestVariance(TestCase):
    def test_variance(self):
        self.assertEqual(format(s.variance([2, 2, 3, 3]), '.5f'), '0.33333')
        self.assertEqual(format(s.variance([0, 0, 5, 5]), '.5f'), '8.33333')
        self.assertEqual(format(s.variance([9, 25, 30, 50, 80, 100, 120, 190, 232, 300, 550]), '.5f'), '25891.21818')

    def test_stddev(self):
        self.assertEqual(format(s.std_dev([2, 2, 3, 3]), '.5f'), '0.57735')
        self.assertEqual(format(s.std_dev([0, 0, 5, 5]), '.5f'), '2.88675')
        self.assertEqual(format(s.std_dev([9, 25, 30, 50, 80, 100, 120, 190, 232, 300, 550]), '.5f'), '160.90748')


