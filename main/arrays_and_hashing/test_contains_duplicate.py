from unittest import TestCase

from main.arrays_and_hashing.contains_duplicate import contains_duplicate


class Test(TestCase):
    def test_duplicate_1_true(self):
        nums = [1,2,3,1]
        self.assertTrue(contains_duplicate(nums))
    def test_triple_duplicate_true(self):
        nums = [1,2,1,1]
        self.assertTrue(contains_duplicate(nums))
    def test_no_duplicates_false(self):
        nums = [1,2,3,4]
        self.assertFalse(contains_duplicate(nums))

    def test_1_size_false(self):
        nums = [0]
        self.assertFalse(contains_duplicate(nums))