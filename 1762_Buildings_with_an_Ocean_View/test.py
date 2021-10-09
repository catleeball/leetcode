import unittest
from collections import deque
from solution import Solution1, Solution0
from absl.testing import parameterized


class TestSolution0(parameterized.TestCase):
    def setUp(self) -> None:
        c = Solution0()
        self.findBuildings = c.findBuildings

    @parameterized.parameters(
        {'heights': [4, 2, 3, 1], 'expected': [0, 2, 3]},
        {'heights': [4, 3, 2, 1], 'expected': [0, 1, 2, 3]},
        {'heights': [1, 3, 2, 4], 'expected': [3]},
        {'heights': [2, 2, 2, 2], 'expected': [3]},
        {'heights': [1], 'expected': [0]},
        {'heights': [], 'expected': []},
    )
    def test_example_1(self, heights, expected):
        actual = self.findBuildings(heights)
        self.assertEqual(expected, actual)


class TestSolution1(parameterized.TestCase):
    def setUp(self) -> None:
        c = Solution1()
        self.findBuildings = c.findBuildings

    @parameterized.parameters(
        {'heights': [4, 2, 3, 1], 'expected': deque([0, 2, 3])},
        {'heights': [4, 3, 2, 1], 'expected': deque([0, 1, 2, 3])},
        {'heights': [1, 3, 2, 4], 'expected': deque([3])},
        {'heights': [2, 2, 2, 2], 'expected': deque([3])},
        {'heights': [1], 'expected': deque([0])},
        {'heights': [], 'expected': deque([])},)
    def test_example_1(self, heights, expected):
        actual = self.findBuildings(heights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
