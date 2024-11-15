class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        twice_appear = []

        # ------------------------------

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                twice_appear.append(nums[i])

        # ------------------------------

        return twice_appear