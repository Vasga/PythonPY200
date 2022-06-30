import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)  # TODO с помощью метода assertIsNone проверить следующий узел
        self.assertIsNone(node.next,msg="При иницализации значения узела")
    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right")
        left_node = Node("left", right_node)

        expected_value = right_node
        actual_value = left_node.next
        # msg = "Значение следующего при инициализации некорректно"
        self.assertIs(expected_value, actual_value, msg="узлы не эквивалентны")
        # self.assertEqual(repr(left_node.next), repr(right_node), msg) # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(5)
        expected_value = "Node(5, None) "# TODO проверить метод __repr__ без следующего узла
        actual_value = repr(node)
        self.assertEqual(expected_value, actual_value, msg="Неправеленый repr")
    ...  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        expected_value = str(some_value)
        self.assertEqual(expected_value, str(node))
        self.assertEqual(expected_value, f"{node}")
        # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(Node(5))  # TODO проверить метод is_valid при корректных узлах
        Node.is_valid(None)

        with self.assertRaises(TypeError):
            invalid_node = "invalid_node"
            Node.is_valid(invalid_node)

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
