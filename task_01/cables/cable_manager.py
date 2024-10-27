"""
Модуль для управління кабелями та розрахунку витрат на їх з'єднання.

Цей модуль містить функцію для обчислення мінімальних витрат на з'єднання 
мережевих кабелів, використовуючи структуру даних "мінімальна купа".
"""

import heapq
from .utils import print_cables, print_heap_state

def minimum_connection_cost(cable_lengths: list[int]) -> int:
    """
    Знаходить мінімальні витрати на з'єднання мережевих кабелів.

    :param cable_lengths: Список довжин мережевих кабелів (int).
    :return: Мінімальні загальні витрати на з'єднання кабелів (int).
    """
    # Виводимо кабелі
    print_cables(cable_lengths)

    # Перетворюємо список у мінімальну купу
    heapq.heapify(cable_lengths)

    # Виводимо стан купи
    print_heap_state(cable_lengths)

    total_cost = 0

    while len(cable_lengths) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # З'єднуємо їх і оновлюємо загальні витрати
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cable_lengths, cost)

    return total_cost
