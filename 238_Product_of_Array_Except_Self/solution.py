"""
Leetcode problem #238: Product of Array Except Self
URL: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
- You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
           (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List, Optional
# import numpy as np
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products: List[int] = []
        for index, _ in enumerate(nums):
            products.append(prod(nums[:index] + nums[index + 1:]))
        return products

    # def numpyProductExceptSelf(self, nums: List[int]) -> List[int]:
    #     total = np.uint32(len(nums))
    #     products = np.empty((total,), dtype=np.int32)
    #     for index, val in enumerate(nums):
    #         products[index] = np.product(
    #             np.asarray((nums[:index] + nums[index+1:]),dtype=np.int32)
    #         )
    #     return np.ndarray.tolist(products)
