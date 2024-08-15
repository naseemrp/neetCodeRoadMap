#https://leetcode.com/problems/two-sum/description/

#brute force and compare each num in nums to find target. time complexity of O(n^2), mem of O(1)
'''
def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i,j]
'''
# using a dictionary

def two_sum(nums, target):
    nums_dic = {}
    for i in range(len(nums)):
        targt = target - nums[i]
        if targt in nums_dic.keys():
            return [i, nums_dic.get(targt)]
        else:
            nums_dic[nums[i]] = i