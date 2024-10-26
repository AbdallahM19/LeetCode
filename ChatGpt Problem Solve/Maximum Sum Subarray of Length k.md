## Task: Maximum Sum Subarray of Length `k`

Given an array of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of length `k`.

### Example:
```plaintext
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The maximum sum of a subarray of length 3 is 5 + 1 + 3 = 9.
```

### Constraints:
- `1 <= k <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Solution Approach:
Use a sliding window of length `k` to calculate the sum of each subarray. Start with the first `k` elements as the initial window, then slide the window by removing the first element of the current window and adding the next element in `nums`. Keep track of the maximum sum found.

### **(My Solution Code)['/ChatGpt Problem Solve/0-main.py']**

### Solution Code:

Here’s how you might solve it:

```python
def max_sum_subarray(nums, k):
    # Initial sum of the first 'k' elements
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window, add the next element and remove the previous one
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # Output should be 9
```

This sliding window approach achieves a time complexity of \(O(n)\), making it efficient even for large arrays.