import unittest
from tree import Tree  # presupunem că fișierul principal se numește tree.py
from node import Node
# caca mare
class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_node(self):
        node = self.tree._find(5, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_find_nonexistent_node(self):
        node = self.tree._find(42, self.tree.getRoot())
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()