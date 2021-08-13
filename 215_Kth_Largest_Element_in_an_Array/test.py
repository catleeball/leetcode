import unittest
from solution import Solution
from typing import List


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.findKthLargest_sort = Solution().findKthLargest_sort
        self.findKthLargest_heap = Solution().findKthLargest_heap

    def test_example_1(self):
        nums: List[int] = [3, 2, 1, 5, 6, 4]
        k: int          = 2
        expected: int   = 5

        sort_solution = self.findKthLargest_sort(nums, k)
        heap_solution = self.findKthLargest_heap(nums, k)
        self.assertEqual(expected, sort_solution)
        self.assertEqual(expected, heap_solution)

    def test_example_2(self):
        nums: List[int] = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k: int          = 4
        expected: int   = 4

        sort_solution = self.findKthLargest_sort(nums, k)
        heap_solution = self.findKthLargest_heap(nums, k)
        self.assertEqual(expected, sort_solution)
        self.assertEqual(expected, heap_solution)


if __name__ == '__main__':
    unittest.main()