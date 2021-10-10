from absl.testing import absltest, parameterized
from solution import SparseVector


class TestSolution(parameterized.TestCase):
    def setUp(self) -> None:
        pass

    @parameterized.parameters(
        {'n1': [1, 0, 0, 2, 3],       'n2': [0, 3, 0, 4, 0],       'expected': 8},  # Example 1
        {'n1': [0, 1, 0, 0, 0],       'n2': [0, 0, 0, 0, 2],       'expected': 8},  # Example 2
        {'n1': [0, 1, 0, 0, 2, 0, 0], 'n2': [1, 0, 0, 0, 3, 0, 4], 'expected': 8},  # Example 3
    )
    def test_sparse_vectors(self, n1, n2, expected):
        v1 = SparseVector(n1)
        v2 = SparseVector(n2)
        actual = v1.dotProduct(v2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    absltest.main()
