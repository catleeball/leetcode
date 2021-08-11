import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.subarraySum = solution.Solution().subarraySum

if __name__ == '__main__':
    unittest.main()