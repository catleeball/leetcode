import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self):
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

    def test_negative(self):
        input = [1, 2, -1, 1, 3]
        k = 3
        expected = 4
        actual = self.subarraySum(input, k)
        self.assertEqual(expected, actual)

    def test_empty(self):
        input = []
        k = 1
        expected = 0
        actual = self.subarraySum(input, k)
        self.assertEqual(expected, actual)

    def test_solution_example(self):
        input = [3, 4, 7, 2, -3, 1, 4, 2]
        k = 7
        expected = 4
        actual = self.subarraySum(input, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
