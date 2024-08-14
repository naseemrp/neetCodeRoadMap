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
# Brute fore method: compare each element with the rest of the element to find a duplicate
# This will have time complexity O(n^2) as it iterates through the list twice. Memory
# complexity is O(1) as there is no additional memory required

'''
def contains_duplicate(nums):
    for i in range(0, len(nums) -1):
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[i]:
                return True
    return False
'''

# Sorting the list, then comparing with the number right next to it will spot the duplicates.
# Sorting always adds a time complexity of O(nlog(n)), mem complexity will be O(1)

'''
def contains_duplicate(nums):
    for i in range(len(nums)-1):
        if (sorted(nums)[i] == sorted(nums)[i+1]):
            return True
    return False
'''

# Using a hashset to use as a comparitor reduces the time complextiy to O(n),
# but the mem complxity increases to O(n)


def contains_duplicate(nums):
    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False
    else:
        return True
