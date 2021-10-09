import unittest
from solution import Solution
from absl.testing import parameterized


class TestSolution(parameterized.TestCase):
    @parameterized.parameters(
        {'heights': [4, 2, 3, 1], 'expected': [0, 2, 3]   },
        {'heights': [4, 3, 2, 1], 'expected': [0, 1, 2, 3]},
        {'heights': [1, 3, 2, 4], 'expected': [3]         },
        {'heights': [2, 2, 2, 2], 'expected': [3]         },
    )
    def setUp(self) -> None:
        self.c = Solution()
        self.findBuildings = Solution.findBuildings

    def test_example_1(self, heights, expected):
        acutal = self.findBuildings(heights)
        self.assertEqual(expected, acutal)


if __name__ == '__main__':
    unittest.main()
