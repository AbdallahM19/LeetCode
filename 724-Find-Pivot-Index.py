class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        for x, i in enumerate(nums):
            total_sum -= i
            if left_sum == total_sum:
                return x
            left_sum += i
        return -1