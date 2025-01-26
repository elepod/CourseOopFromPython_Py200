from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        # TODO инициализировать атрибуты value и next экземпляра класса Node
        self.value = value
        self.next = next_


    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {self.next})"


if __name__ == '__main__':
    first_node = Node(1)  # TODO инициализировать первый узел со значением 1

    second_node = Node(2)  # TODO инициализировать второй узел со значением 2
    first_node.next = second_node  # TODO через атрибут экземпляра устанавливаем первому узлу следующий узел

    print(first_node)
    print(second_node)
