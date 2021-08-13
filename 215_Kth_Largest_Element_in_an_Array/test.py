import unittest
from solution import Solution
from typing import List


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.minRemoveToMakeValid = Solution().findKthLargest

    def test_example_1(self):
        nums: List[int] = [3, 2, 1, 5, 6, 4]
        k: int          = 2
        expected: int   = 5
        actual = self.findKthLargest(nums, k)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        nums: List[int] = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k: int          = 4
        expected: int   = 4
        actual = self.findKthLargest(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()