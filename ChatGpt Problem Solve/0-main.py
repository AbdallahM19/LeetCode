"""0-main.py"""

from typing import List


def max_sum_subarray(nums_array: List[int], k_element: int) -> int:
    """Find the maximum sum of a subarray of size k in the given list of integers."""
    result_sum = sum(nums_array[:k_element])
    res_max = result_sum

    for i in range(k_element, len(nums_array)):
        result_sum += nums_array[i] - nums_array[i - k_element]
        res_max = max(result_sum, res_max)

    return res_max


# Example usage:
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # Output should be 9
