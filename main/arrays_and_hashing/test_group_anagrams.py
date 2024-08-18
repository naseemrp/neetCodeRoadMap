from unittest import TestCase

from main.arrays_and_hashing.group_anagrams import groupAnagrams


class Test(TestCase):
    def test_group_anagrams(self):
        self.assertEqual(groupAnagrams(['hi', 'ih']), [['hi', 'ih']])
