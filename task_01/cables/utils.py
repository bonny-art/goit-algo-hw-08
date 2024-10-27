"""
Модуль для допоміжних функцій в управлінні кабелями.

Цей модуль містить функції для виведення інформації про кабелі та 
стан купи.
"""

def print_cables(cable_lengths: list[int]) -> None:
    """
    Виводить наявні кабелі у форматі з вирівнюванням.

    :param cable_lengths: Список довжин мережевих кабелів (int).
    """
    print("Наявні кабелі:")

    max_length = max(cable_lengths, default=0)  # Максимальна довжина кабелів для вирівнювання

    for length in cable_lengths:
        print(f"{str(length).rjust(len(str(max_length)))}: {'-' * length}")

def print_heap_state(cable_lengths: list[int]) -> None:
    """
    Виводить стан купи після heapify.

    :param cable_lengths: Список довжин мережевих кабелів (int).
    """
    print("\nСтан купи після heapify:")
    print(cable_lengths)  # Показує внутрішнє представлення купи
