"""
Головний модуль програми для розрахунку витрат на з'єднання мережевих кабелів.

Цей модуль запускає програму, імплементуючи основну логіку 
з'єднання кабелів та виведення результатів.
"""

from cables.cable_manager import minimum_connection_cost

# Приклад використання
cables = [8, 4, 6, 12, 2, 9, 7, 10, 3, 2]
min_cost = minimum_connection_cost(cables)
print(f"\nМінімальні загальні витрати на з'єднання: {min_cost}")

# todo: Додати візуалізацію купи синіми кружечками