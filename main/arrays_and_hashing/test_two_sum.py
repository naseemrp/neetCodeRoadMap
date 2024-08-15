from unittest import TestCase

from main.arrays_and_hashing.two_sum import two_sum


class Test(TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
    def test_two_num(self):
        self.assertEqual(two_sum([2,7], 9), [0,1])
    def test_two_num_2(self):
        self.assertEqual(two_sum([2,2], 4), [0,1])
