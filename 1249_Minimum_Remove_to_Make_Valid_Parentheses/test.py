import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.minRemoveToMakeValid = Solution().minRemoveToMakeValid

    # TODO: These tests could be refactored into a smarter solver that checks if parens are valid and all the characters
    #       are still present. Currently, there could be other valid solutions to these tests, and making tests to
    #       account for all possible outputs could grow very large.

    def test_example_1(self):
        input_string = "lee(t(c)o)de)"
        # Any of following are acceptable outputs.
        expected = ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]
        actual = self.minRemoveToMakeValid(input_string)
        self.assertIn(actual, expected)

    def test_example_2(self):
        input_string = "a)b(c)d"
        expected = "ab(c)d"
        actual = self.minRemoveToMakeValid(input_string)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        input_string = "))(("
        expected = ""
        actual = self.minRemoveToMakeValid(input_string)
        self.assertEqual(expected, actual)

    def test_example_4(self):
        input_string = "(a(b(c)d)"
        expected = ["a(b(c)d)", "(a(bc)d)"]
        actual = self.minRemoveToMakeValid(input_string)
        self.assertIn(actual, expected)

    def test_one_paren(self):
        input_string = '(a'
        expected = 'a'
        actual = self.minRemoveToMakeValid(input_string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()