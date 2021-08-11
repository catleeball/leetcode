import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.subarraySum = solution.Solution().subarraySum

    def test_example_1(self):
        input_string = "lee(t(c)o)de)"
        # Any of following are acceptable outputs.
        expected = ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]

    def test_example_2(self):
        input_string = "a)b(c)d"
        expected = "a)b(c)d"

    def test_example_3(self):
        input_string = "))(("
        expected = ""

    def test_example_4(self):
        input_string = "(a(b(c)d)"
        expected = "a(b(c)d)"


if __name__ == '__main__':
    unittest.main()