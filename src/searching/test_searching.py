import unittest


class SearchingTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.TEST_VALUES = (
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 6, -1),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -9, 0),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 0, 6),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 9, 13),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8], -9, 0),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8], -2, 5),
            ([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8], 8, 12),
            ([], 0, -1)
        )

    def test_linear_search(self):
        from searching import linear_search

        for TEST_VALUE in self.TEST_VALUES:
            self.assertEqual(
                linear_search(TEST_VALUE[0], TEST_VALUE[1]),
                TEST_VALUE[2]
            )

    def test_binary_search(self):
        from searching import binary_search

        for TEST_VALUE in self.TEST_VALUES:
            self.assertEqual(
                binary_search(TEST_VALUE[0], TEST_VALUE[1]),
                TEST_VALUE[2]
            )

    def test_binary_search_recursive(self):
        from searching import binary_search_recursive

        for TEST_VALUE in self.TEST_VALUES:
            self.assertEqual(
                binary_search_recursive(TEST_VALUE[0], TEST_VALUE[1]),
                TEST_VALUE[2]
            )


if __name__ == '__main__':
    unittest.main()
