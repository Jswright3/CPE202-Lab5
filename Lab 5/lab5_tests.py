"""CPE202
John Wright
Lab 5
"""
import unittest
from lab5 import *
from bst import *

class MyTest(unittest.TestCase):

   def test_BSTNode(self):
      t = None
      t = insert(t, 4, 'four')
      t = insert(t, 2, 'two')
      t = insert(t, 3, 'three')
      t = insert(t, 1, 'one')
      t = insert(t, 7, 'seven')
      t = insert(t, 5, 'five')
      t = insert(t, 6, 'six')
      self.assertEqual(t.right.left.right.key, 6)
      self.assertEqual(t.right.key, 7)
      self.assertEqual(t.left.key, 2)
      self.assertEqual(tree_height(t), 3)
      t = delete(t, 6)
      self.assertEqual(t.key, 4)
      self.assertEqual(t.left.key, 2)
      self.assertEqual(t.right.key, 7)
      self.assertEqual(t.right.left.key, 5)
      self.assertEqual(tree_height(t),2)
      self.assertEqual(find_min(t), (1, 'one'))
      self.assertEqual(find_max(t), (7, 'seven'))

   def test_classmates(self):
      filename = '/Users/Johnsw/Desktop/CPE202/Lab 5/classmates.tsv'
      t = import_classmates(filename)
      self.assertRaises(KeyError, search_classmate, t, 0)
      self.assertEqual(t.size(), 38)
      v = search_classmate(t, 24)
      self.assertEqual(v.major, 'EE')

if __name__ == '__main__':
   unittest.main()
