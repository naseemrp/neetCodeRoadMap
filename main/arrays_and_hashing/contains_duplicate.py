# https://leetcode.com/problems/contains-duplicate

#this solution works with small size of nums
'''
def contains_duplicate(nums):
    if len(nums) <= 1:
        return False
    cache = []
    for num in nums:
        if num in cache:
            return True
        cache.append(num)
    return False
'''
def contains_duplicate(nums):
    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False
    else:
        return True