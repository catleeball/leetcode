# 1570. Dot Product of Two Sparse Vectors
# ----------------------------------------------------------------------------------------------------------------------
# Given two sparse vectors, compute their dot product.
#
# Implement class SparseVector:
#     SparseVector(nums) Initializes the object with the vector nums
#     dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
#
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute
# the dot product between two SparseVector.
#
# Follow up: What if only one of the vectors is sparse?
# ----------------------------------------------------------------------------------------------------------------------
# Example 1:
#     Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
#     Output: 8
#     Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
#     v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
#
# Example 2:
#     Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
#     Output: 0
#     Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
#     v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
#
# Example 3:
#     Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
#     Output: 6
# ----------------------------------------------------------------------------------------------------------------------
# Constraints:
#     n == nums1.length == nums2.length
#     1 <= n <= 10^5
#     0 <= nums1[i], nums2[i] <= 100
# ----------------------------------------------------------------------------------------------------------------------

from typing import List


# Runtime: 2181 ms, faster than 32.68% of Python3 online submissions for Dot Product of Two Sparse Vectors.
# Memory Usage: 37.8 MB, less than 5.93% of Python3 online submissions for Dot Product of Two Sparse Vectors.
class SparseVector:
    def __init__(self, nums: List[int]):
        self.IndexValueMap = {}
        for index, value in enumerate(nums):
            self.IndexValueMap[index] = value

    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for index in vec.IndexValueMap:
            # Both vectors must have a value at the same index to return a value, since 0 * anything = 0.
            if index in self.IndexValueMap:
                dot_product += self.IndexValueMap[index] * vec.IndexValueMap[index]
        return dot_product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
