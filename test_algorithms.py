import unittest
import timeit

from algorithms import bubble_sort, selection_sort, insertion_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        # Test cases: sorted, reverse sorted, random
        self.test_cases = {
            "sorted": [list(range(10)), list(range(100)), list(range(1000))],
            "reverse_sorted": [list(range(9, -1, -1)), list(range(99, -1, -1)), list(range(999, -1, -1))],
            "random": [[64, 34, 25, 22, 12, 90, 11], [64, 34, 25, 12, 22, 11, 90], [90, 11, 25, 12, 22, 34, 64]]
        }

    def test_bubble_sort(self):
        self._test_algorithm(bubble_sort, "Bubble Sort")

    def test_selection_sort(self):
        self._test_algorithm(selection_sort, "Selection Sort")

    def test_insertion_sort(self):
        self._test_algorithm(insertion_sort, "Insertion Sort")

    def _test_algorithm(self, algorithm, algorithm_name):
        print(f"\nTesting {algorithm_name}...")
        for case_name, cases in self.test_cases.items():
            for case in cases:
                arr_copy = case[:]
                start_time = timeit.default_timer()
                sorted_array, swap_count = algorithm(arr_copy)
                elapsed = timeit.default_timer() - start_time
                
                print(f"{algorithm_name} - {case_name} - Size: {len(case)}")
                print(f"Time: {elapsed:.6f}s, Swaps: {swap_count}, Sorted: {sorted_array == sorted(case)}")

if __name__ == '__main__':
    unittest.main()