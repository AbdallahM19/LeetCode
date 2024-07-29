class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 1
        for i in nums:
            sums *= i
        return 1 if sums > 0 else 0 if sums == 0 else -1