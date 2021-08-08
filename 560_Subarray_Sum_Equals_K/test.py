import unittest
import solution


class TestSolution(unittest.TestCase):

    def SetUp(self):
        self.subarraySum = solution.Solution().subarraySum

    def test_example_1(self):
        input = [1, 1, 1]
        k = 2
        expected = 2
        actual = self.subarraySum(input, k)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        input = [1, 2, 3]
        k = 3
        expected = 2
        actual = self.subarraySum(input, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
