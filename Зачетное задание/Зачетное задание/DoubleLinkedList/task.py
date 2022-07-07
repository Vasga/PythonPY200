from collections.abc import MutableSequence
from typing import Any, Optional

from node import Node


class LinkedList(MutableSequence):
    def __init__(self, data=None):
        self.len = 0
        self.head: Optional[Node] = None
        super(LinkedList, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()


    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        return self._list[index]

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        self._list[index] = value

    def __delitem__(self, index: int) -> None:
        del self._list[index]

    def __len__(self) -> int:
        return self.len


    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __str__(self):
        return str(self._list)

    def insert(self, index: int, value: Any) -> None:
        self._list.insert(index, value)

    def append(self, val):
        self.insert(len(self._list), val)


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    list_ = [1, 2, 3]
    ll = LinkedList(list_)
    print(ll)
    print(repr(ll))

    ll.append(5)
    print(ll)
    print(repr(ll))
    ll.insert(3,"woe")
    print(ll)
    print(repr(ll))
    ll.__delitem__(3)
    print(ll)
    print(repr(ll))
    ll.__setitem__(3,66)
    print(repr(ll))