class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a, i in enumerate(nums):
            for b, x in enumerate(nums):
                if i + x == target and a != b:
                    return [a, b]