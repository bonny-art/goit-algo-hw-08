"""
Модуль для об'єднання декількох відсортованих списків у один відсортований список
з використанням мінімальної купи для підвищення ефективності.

Цей модуль містить функцію `merge_k_sorted_lists`, яка приймає список відсортованих
списків і повертає єдиний відсортований список, що містить усі елементи початкових списків.
"""

import heapq
from typing import List, Tuple

def merge_k_sorted_lists(sorted_lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків у один відсортований список.

    Використовує мінімальну купу для витягання найменших елементів серед
    усіх списків, забезпечуючи тим самим ефективність алгоритму O(N log k),
    де N — загальна кількість елементів, а k — кількість списків.

    :param sorted_lists: Список k відсортованих списків цілих чисел.
    :type sorted_lists: List[List[int]]
    :return: Відсортований список, що містить усі елементи з `sorted_lists`.
    :rtype: List[int]
    """
    # Ініціалізація мінімальної купи з першими елементами всіх списків
    min_heap: List[Tuple[int, int, int]] = []

    for i, lst in enumerate(sorted_lists):
        if lst:  # Перевірка на порожні списки
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)

    merged_result: List[int] = []

    # Проходимо через мінімальну купу, поки вона не порожня
    while min_heap:
        # Витягуємо найменший елемент з купи
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_result.append(value)

        # Якщо є наступний елемент у тому ж списку, додаємо його до купи
        if element_index + 1 < len(sorted_lists[list_index]):
            next_value = sorted_lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_result
