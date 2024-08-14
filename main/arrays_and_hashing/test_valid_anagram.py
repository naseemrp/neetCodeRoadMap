from unittest import TestCase

from main.arrays_and_hashing.valid_anagram import isAnagram


class Test(TestCase):

    def test_diff_size_false(self):
        self.assertFalse(isAnagram("bc", "bca"))
    def test_is_anagram(self):
        self.assertTrue(isAnagram("abc", "bca"))

    def test_1_letter_string_true(self):
        self.assertTrue(isAnagram("a", "a"))

    def test_1_letter_string_false(self):
        self.assertFalse(isAnagram("a", "b"))

    def test_2_letter_string_true(self):
        self.assertTrue(isAnagram("ab", "ba"))
        self.assertTrue(isAnagram("aa", "aa"))

    def test_2_letter_string_false(self):
        self.assertFalse(isAnagram("ab", "cd"))
        self.assertFalse(isAnagram("ab", "bc"))

