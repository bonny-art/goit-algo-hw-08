"""
Модуль для управління мережевими кабелями, включаючи побудову мінімальної купи,
візуалізацію та розрахунок мінімальних витрат на з'єднання кабелів.
"""

import heapq
from .utils import print_cables, print_heap_state
from .visualizer import Node, draw_tree

def build_heap_tree(heap: list[int], index: int = 0) -> Node | None:
    """
    Рекурсивно будує дерево з масиву купи.

    :param heap: Масив, що представляє купу.
    :param index: Індекс поточного елемента в масиві.
    :return: Корінь дерева (Node) або None, якщо індекс виходить за межі.
    """
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node

def heap_visual(heap_array: list[int], filename: str, title: str) -> None:
    """
    Візуалізує купу у вигляді дерева та зберігає у файл.

    :param heap_array: Масив, що представляє купу.
    :param filename: Ім'я файлу для збереження зображення.
    :param title: Заголовок для графіку.
    """
    if not heap_array:
        print("Heap is empty")
        return
    heap_tree_root = build_heap_tree(heap_array)
    draw_tree(heap_tree_root, filename, title)

def minimum_connection_cost(cable_lengths: list[int]) -> int:
    """
    Знаходить мінімальні витрати на з'єднання мережевих кабелів.

    :param cable_lengths: Список довжин мережевих кабелів (int).
    :return: Мінімальні загальні витрати на з'єднання кабелів (int).
    """
    print_cables(cable_lengths)
    heap_visual(cable_lengths, "task_01/heap_tree_before_heapify.png", "Купа перед heapify")

    # Перетворюємо список у мінімальну купу
    heapq.heapify(cable_lengths)

    print_heap_state(cable_lengths)
    heap_visual(cable_lengths, "task_01/heap_tree_after_heapify.png", "Купа після heapify")

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
