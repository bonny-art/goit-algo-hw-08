"""
Модуль для візуалізації деревоподібних структур.

Цей модуль містить класи та функції для побудови та малювання
деревоподібних структур, використовуючи бібліотеки networkx та matplotlib.
"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """
    Клас, що представляє вузол дерева.

    Кожен вузол має значення, колір, унікальний ідентифікатор,
    а також посилання на лівий та правий дочірні вузли.
    """

    def __init__(self, key: int, color: str = "skyblue"):
        """
        Ініціалізація вузла дерева.

        :param key: Значення, яке зберігається в вузлі.
        :param color: Колір вузла для візуалізації.
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def add_edges(graph: nx.DiGraph, node: Node, pos: dict, x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """
    Додає ребра до графа на основі дерева.

    :param graph: Граф, до якого додаються ребра.
    :param node: Вузол дерева, з якого починається додавання.
    :param pos: Позиції вузлів для візуалізації.
    :param x: Координата x для позиції вузла.
    :param y: Координата y для позиції вузла.
    :param layer: Шар дерева, для обчислення позицій дочірніх вузлів.
    :return: Граф з доданими ребрами.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, filename: str, title: str, width: int = 8, height: int = 6, top_margin: float = 2):
    """
    Малює дерево та зберігає його у файл.

    :param tree_root: Корінь дерева, яке потрібно намалювати.
    :param filename: Назва файлу для збереження зображення.
    :param title: Заголовок, який буде відображено на графіку.
    :param width: Ширина фігури у дюймах.
    :param height: Висота фігури у дюймах.
    :param top_margin: Відстань від верхнього краю фігури до верхньої межі графіка.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(width, height))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.suptitle(title)

    lower_limit = -height + top_margin  # Обчислюємо нижню межу графіка

    plt.ylim(lower_limit, 1)  # Встановлюємо межі осі Y

    plt.savefig(filename)  # Зберігаємо графік у файл
    plt.close()  # Закриваємо фігуру
