class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k
            if cumulative_sum in remainder_map:
                if i - remainder_map[cumulative_sum] > 1:
                    return True
            else:
                remainder_map[cumulative_sum] = i
        return False
        