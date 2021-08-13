import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.productExceptSelf = Solution().productExceptSelf

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(
            self.productExceptSelf(nums),
            expected
        )

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(
            self.productExceptSelf(nums),
            expected
        )


if __name__ == '__main__':
    unittest.main()
