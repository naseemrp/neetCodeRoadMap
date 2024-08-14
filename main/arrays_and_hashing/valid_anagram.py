# https://leetcode.com/problems/valid-anagram/description/

#Sorted and compare. You can sort both lists, then compare each element, this will give time
#complexity O(2nlog(n)). mem complexity will be O(1)
'''
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if sorted(s)[i] != sorted(t)[i]:
            return False
    return True
'''
# Creating a hashmap/dictionary will list all of the char and the count, then can iterate through
# the next list and subtract the count. time complex will be O(n), mem will be O(n)

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    dic = dict()
    for i in range(len(s)):
        dic[s[i]] = 1 + dic.get(s[i], 0)
        dic[t[i]] = dic.get(t[i], 0) -1
    for k, v in dic.items():
        if v != 0:
            return False
    return True