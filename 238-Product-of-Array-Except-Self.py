class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0] * n
        left[0] = 1
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        right = [0] * n
        right[-1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        answer = [0] * n
        for i in range(n):
            answer[i] = left[i] * right[i]
        return answer