# error 1
# Line 23: TypeError: reduce() of empty sequence with no initial value
from functools import reduce
class Solution(object):
    def common(self, str1, str2):
        i = -1
        index1 = len(str1) - 1
        index2 = len(str2) - 1
        if index1 > index2:
            index = index2
        else:
            index = index1
        while i < index:
            if str1[i+1] == str2[i+1]:
                i = i + 1
            else:
                break
        return str1[0:i+1]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        else:
            longest_common = reduce(self.common, strs)
            return longest_common

my_solution = Solution()
strs = ['c', 'c']
print(my_solution.longestCommonPrefix(strs))
strs = ['ok', 'okmy']
print(my_solution.longestCommonPrefix(strs))
