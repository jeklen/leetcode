"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        dict = {}
        for k, v in enumerate(nums):
            print("k = ", k, "v = ", v)
            pair = target - v
            if pair in dict:
                return [dict[pair], k]
            else:
                dict[v] = k
        return []
'''        
        for k, v in enumerate(nums):
            if k in dict:
                dict[]
                ...
            else:
                dict[v] = k
        for key in dict.keys():
            pair = target - key
            if pair in dict:
                return [dict[key], dict[pair]]
        return []
'''

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
