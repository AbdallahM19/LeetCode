class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        array = {}
        for i in nums:
            if i in array:
                array[i] += 1
            else:
                array[i] = 1
        sorted_array = sorted(array, key=array.get, reverse=True)
        return sorted_array[:k]