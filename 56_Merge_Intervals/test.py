import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution_class = solution.Solution()
        self.merge = self.solution_class.merge

    def test_example_1(self):
        # Example 1 from the Leetcode problem.
        intervals       = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected_output = [[1, 6], [8, 10], [15, 18]]
        actual_output = self.merge(intervals)
        self.assertEqual(expected_output, actual_output)

    def test_example_2(self):
        # Example 2 from the Leetcode problem.
        intervals       = [[1, 4], [4, 5]]
        expected_output = [[1, 5]]
        actual_output = self.merge(intervals)
        self.assertEqual(expected_output, actual_output)

    def test_edge_case_one_item(self):
        intervals       = [[1, 2]]
        expected_output = [[1, 2]]
        actual_output = self.merge(intervals)
        self.assertEqual(expected_output, actual_output)

    def test_edge_case_zero_items(self):
        intervals       = [[]]
        expected_output = [[]]
        actual_output = self.merge(intervals)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()