"""Contains starter code for lab 5

CPE202

Instructions:
    Complete this file by writing python3 code.

"""
import random

#implement BSTNode class and get,contains,insert,delete functions in bst.py
import bst

#classmate.py is implemented for you
from classmate import classmate_factory


class TreeMap:
    """Map of Binary Search tree
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return bst.inorder_list(self.tree)

    def __eq__(self, other):
        if self.tree == other.tree:
            return True
        return False

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.
        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py
        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def get(self, key):
        """put a key value pair into the map
        Calls insert function in bst.py
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with th key
        """
        return bst.get(self.tree, key)

    def contains(self, key):
        """Checks if key is in BST
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """Deletes key and its Node from BST
        Args:
            key (any) : a key which is compareable by <,>,==
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1


    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self):
        """Finds Smallest Key in the tree
        Returns:
            key (int), val (any
        """
        return bst.find_min(self.tree)

    def find_max(self):
        """Return Max of Tree
        Returns:
            (int) max ket
        """
        return bst.find_max(self.tree)

    def inorder_list(self):
        """Returns inorder traversal of tree
        Returns:
            (list) list of keys of tree.
        """
        return bst.inorder_list(self.tree)

    def preorder_list(self):
        """Returns preorder traversal of tree
        Returns:
            (list) list of keys of tree.
        """
        return bst.preorder_list(self.tree)

    def tree_height(self):
        """Returns tree height
        Returns:
            int: tree height
        """
        return bst.tree_height(self.tree)

    def range_search(self, low, high):
        """Returns list of keys in range from tree
        Returns:
            (list) keys in range
        """
        return bst.range_search(self.tree, low, high)

def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    #---- to do ----
    # complete this function by following the comments below
    #
    #open the file whose name is passed as the argument filename
    # with python builtin open() function.
    #read all lines in the file and assign it to variable lines
    #for each line in lines
        #split the line at tabs (\t) and assign it to a variable tokens
        #classmate = classmate_factory(tokens)
        #append the classmate to a list classmates
    #---------- ----
    lines = open(filename, 'r')
    for line in lines:
        tokens = line.split('\t')
        classmate = classmate_factory(tokens)
        classmates.append(classmate)

    #shuffle the classmates
    random.seed(2)
    random.shuffle(classmates)

    #---- to do ----
    # complete this function by following the comments below
    #
    #for each classmate in classmates
        #put the classmate into the tree_map using its id as the key
    #---------- ----
    for classmate in classmates:
        tree_map.put(classmate.sid, classmate)
    return tree_map

def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the id as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    if sid in tmap:
        return tmap[sid]
    raise KeyError("A classmate with the id: %d does not exist!" % (sid))
