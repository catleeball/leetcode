from typing import Dict, List

# Leetcode question: 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.

from collections import defaultdict

class Solution:
    # Leetcode's evaluation of this solution:
    #   Runtime:       248 ms, faster than 85.93% of Python3 online submissions for Subarray Sum Equals K.
    #   Memory Usage: 16.7 MB, less than   61.33% of Python3 online submissions for Subarray Sum Equals K.
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Edge case: empty list.
        if not nums:
            return 0

        # Edge case: single int in list.
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0

        count: int = 0
        cumulative_sum: int = 0

        # Map distinct cumulative sums as keys, frequencies of those sums as values
        sums: Dict[int, int] = defaultdict(int)
        sums[0] = 1

        # Loop over given input numbers, adding them into cumulative_sum, and placing them into the dict sums.
        for num in nums:
            cumulative_sum += num
            # Subtracting target sum K yields the compliment for the current iteration of the list; e.g. you can
            # infer if there would be a valid start pointer for this given end pointer by checking if the compliment
            # is already in the dictionary.
            if cumulative_sum - k in sums:
                count += sums[cumulative_sum - k]
            sums[cumulative_sum] += 1

        return count
