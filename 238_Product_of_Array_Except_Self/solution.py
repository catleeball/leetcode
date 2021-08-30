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
import array
from typing import List, Iterable
from math import prod


class Solution:
    # Optimization note: Could write special path for zeros.
    #                    Also, if there's ever more than one zero in nums, the return is all zeros.

    def lr_product(self, nums: Iterable) -> Iterable:
        products = array.array('i')
        for index, value in enumerate(nums):
            if index == 0:
                # This value will later be replaced by the product of all rightmost elements.
                products.append(1)
                continue

            if index == 1:
                products.append(value)
                continue

            if index == len(nums) - 1:
                # We never want the product of all list items.
                break

            # I hate that this is faster than just `products.append(products[-1] * value)` but here we are.
            products.append(prod(array.array('i', (products[index - 1], value))))

        return products

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Solution to problem stated at top of file."""

        # Don't do any math if it's just two items.
        if len(nums) == 2:
            return [nums[1], nums[0]]

        # Extra O(n) compute, going to benchmark if this helps product speed any.
        nums_arr = array.array('i', nums)
        # Peak memory under O(n*2) until we drop `nums`. We don't bother popping the list down to avoid the memory peak
        # since array.fromlist is defined in arraymodule.c and we'll avoid hopping around a lot of interpreted popping
        # and save overall compute time.
        del nums

        # TODO: reduce memory overhead.
        left_products = self.lr_product(nums_arr)
        left_products.reverse()
        nums_arr.reverse()
        right_products = self.lr_product(nums_arr)

        for index, _ in enumerate(nums_arr):
            if index == 0:
                nums_arr[0] = right_products.pop()
                continue
            if index == len(nums_arr) - 1:
                nums_arr[index] = left_products.pop()
                break
            nums_arr[index] = prod(array.array('i', (right_products.pop(), left_products.pop())))

        return nums_arr.tolist()


        # In-place attempt, broken
        # current_right_product = 1
        # prev_right_val = None
        # i = len(nums_arr) - 1
        # while left_products:
        #     n = left_products.pop()
        #     if not prev_right_val:
        #         prev_right_val = nums_arr[i]
        #         nums_arr[i] = n
        #         continue
        #     current_right_product = prod(array.array('i', (n, current_right_product)))
        #     prev_right_val = nums_arr[i]
        #     nums_arr[i] = current_right_product
        #     i -= 1
            # products.append(self.cached_product(left=nums_arr[:index], right=nums_arr[index + 1:]))