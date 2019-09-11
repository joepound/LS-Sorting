import unittest
from random import sample
from copy import deepcopy


class RecursiveSortingTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.UNSORTED_TEST_LISTS = (
            [1, 5, 8, 4, 2, 9, 6, 0, 3, 7],
            [],
            [9000],
            [1, 5, 8, 8, 4, 2, 9, 2, 6, 0, 3, 7],
            sample(range(1000), 250)
        )
        self.SORTED_TEST_LISTS = tuple(
            sorted(LIST) for LIST in self.UNSORTED_TEST_LISTS
        )

    def test_merge_sort(self):
        from recursive_sorting import merge_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            self.assertEqual(
                merge_sort(test_lists[i]),
                self.SORTED_TEST_LISTS[i]
            )

    # Uncomment this test to test your in-place merge sort implementation

    def test_in_place_merge_sort(self):
        from recursive_sorting import merge_sort_in_place

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            merge_sort_in_place(test_lists[i], 0, len(test_lists[i]) - 1)
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])

    def test_timsort(self):
        from recursive_sorting import timsort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            timsort(test_lists[i])
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])

    def test_quick_sort(self):
        from recursive_sorting import quick_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            self.assertEqual(
                quick_sort(test_lists[i]),
                self.SORTED_TEST_LISTS[i]
            )


if __name__ == '__main__':
    unittest.main()
