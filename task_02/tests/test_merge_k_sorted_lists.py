"""
Модуль для тестування функції merge_k_sorted_lists, яка об'єднує k відсортованих списків у один відсортований список.

Цей модуль містить кілька тестових випадків для перевірки коректності роботи функції merge_k_sorted_lists.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from merge_k_sorted_lists import merge_k_sorted_lists



class TestMergeKSortedLists(unittest.TestCase):
    """
    Набір тестів для функції merge_k_sorted_lists, яка об'єднує k відсортованих списків у один відсортований список.
    """

    def test_merge_k_sorted_lists(self):
        """
        Перевіряє коректність об'єднання кількох відсортованих списків у один відсортований список.
        """
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        result = merge_k_sorted_lists(lists)
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(result, expected)

    def test_empty_lists(self):
        """
        Перевіряє поведінку функції при передачі списку з кількома порожніми списками.
        """
        lists = [[], [], []]
        result = merge_k_sorted_lists(lists)
        expected = []
        self.assertEqual(result, expected)

    def test_single_element_lists(self):
        """
        Перевіряє коректність об'єднання списків, які містять по одному елементу кожен.
        """
        lists = [[1], [2], [3]]
        result = merge_k_sorted_lists(lists)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
