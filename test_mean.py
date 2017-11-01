from unittest import TestCase
import mean as m

class TestMean(TestCase):
    
    def test_sum(self):
        self.assertEqual(m.sum([1,2,3,4,5,6]),21)
        self.assertEqual(m.sum([1,2]),3)

    def test_mean(self):
        self.assertEqual(m.mean([1,2]),1.5)
        self.assertEqual(m.mean([1,2,3,4]),2.5)


