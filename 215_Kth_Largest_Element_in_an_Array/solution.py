"""
Leetcode problem #215: Kth Largest Element in an Array
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints:
    1 <= k <= nums.length <= 104
    -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq


class Solution:
    # Sort solution. Compute: O(n log n), Memory: O(1)
    # Stats from Leetcode:
    #     Runtime:       140 ms, faster than 17.27% of Python3 online submissions for Kth Largest Element in an Array.
    #     Memory Usage: 15.1 MB, less than   45.82% of Python3 online submissions for Kth Largest Element in an Array.
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    # Heapq solution. Compute: O(n log k), Memory: O(k)
    # Stats from Leetcode:
    #     Runtime:        64 ms, faster than 70.63% of Python3 online submissions for Kth Largest Element in an Array.
    #     Memory Usage: 15.1 MB, less than 75.49%   of Python3 online submissions for Kth Largest Element in an Array.
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # TODO: Quickselect solution (https://en.wikipedia.org/wiki/Quickselect).
