import unittest
from random import sample
from copy import deepcopy


class IterativeSortingTest(unittest.TestCase):
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

    def test_selection_sort(self):
        from iterative_sorting import selection_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            selection_sort(test_lists[i])
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])

    def test_bubble_sort(self):
        from iterative_sorting import bubble_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            bubble_sort(test_lists[i])
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])

    # Uncomment this test to test your count_sort implementation

    def test_count_sort(self):
        from iterative_sorting import count_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            count_sort(test_lists[i])
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])

    def test_insertion_sort(self):
        from iterative_sorting import insertion_sort

        test_lists = deepcopy(self.UNSORTED_TEST_LISTS)
        for i in range(len(test_lists)):
            insertion_sort(test_lists[i])
            self.assertEqual(test_lists[i], self.SORTED_TEST_LISTS[i])


if __name__ == '__main__':
    unittest.main()
