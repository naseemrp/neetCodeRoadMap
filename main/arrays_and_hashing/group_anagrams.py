#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict

from main.arrays_and_hashing.valid_anagram import isAnagram


def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()

print(groupAnagrams(['hi', 'ih']))