"""Module for BST
CPE202
John Wright

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.
"""
class BSTNode:
    """Binary Search Tree Node class.
    Attributes:
        key (any)
        val (any)
        left (BSTNode)
        right (BSTNode).
    """
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __repr(self):
        pass

    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False

def get(tree, key):
    """Get val from given key in BST
    Args:
        tree (BSTNode): Our BST
        key (int): key of BSTNode to get
    Returns:
        (any): Value stored in BSTNode
    """
    if tree is None:
        raise KeyError()
    if tree.key == key:
        return tree.val
    if tree.key < key:
        return get(tree.right, key)
    return get(tree.left, key)

def contains(tree, key):
    """Checks if key is in BST
    Returns:
        (Bool)
    """
    if tree is None:
        return False
    if key == tree.key:
        return True
    if key < tree.key:
        return get(tree.left, key)
    return get(tree.right, key)

def insert(tree, key, val):
    """insert a key value pair node into the Binary Search Tree
    Args:
        tree (BSTNode):
        key (any):
        val (any):
    """
    if tree is None:
        tree = BSTNode(key, val)
    else:
        if key < tree.key:
            tree.left = insert(tree.left, key, val)
        else:
            tree.right = insert(tree.right, key, val)
    return tree

def delete(tree, key):
    """Deletes key from BST
    Args:
        tree (BSTNode): Our BST
        key (any): Key of Node to delete
    Returns:
        (BSTNode) BST
    """
    if tree is None:
        return None
    if tree.key == key:
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        rep = get_rep(tree.right)
        tree = delete(tree, rep.key)
        tree.key, tree.val = rep.key, rep.val
        return tree
    if tree.key > key:
        tree.left = delete(tree.left, key)
    if tree.key < key:
        tree.right = delete(tree.right, key)
    return tree

def get_rep(tree):
    """Get replacement function for delete, gets lowest number in right side
    Returns:
        (BSTNode) replacement node
    """
    if tree is None:
        return None
    if tree.left is None:
        return tree
    return get_rep(tree.left)

def find_min(tree):
    """Returns key and value of smallest key in BST
    Returns:
        (int), (any) key and val
    """
    if tree.left is None:
        return tree.key, tree.val
    return find_min(tree.left)

def find_max(tree):
    """Returns key and value of largest key in BST
    Returns:
        (int), (any) key and val
    """
    if tree.right is None:
        return tree.key, tree.val
    return find_max(tree.right)

def inorder_list(tree):
    """returns list of inorder traversal of BST
    Returns:
        (list)
    """
    if tree is None:
        return []
    left = inorder_list(tree.left)
    right = inorder_list(tree.right)
    return left + [tree.key] + right

def preorder_list(tree):
    """returns list of preorder traversal of BST
    Returns:
        (list)
    """
    if tree is None:
        return []
    left = preorder_list(tree.left)
    right = preorder_list(tree.right)
    return [tree.key] + left + right

def tree_height(tree):
    """Finds height of BST
    Returns:
        (int): height of BST
    """
    if tree is None:
        return -1
    if tree.left is None:
        return tree_height(tree.right) + 1
    if tree.right is None:
        return tree_height(tree.left) + 1
    return max(tree_height(tree.left), tree_height(tree.right)) + 1

def range_search(tree, lo, hi, accum=[]):
    """Takes range and searches BST, returns values from all keys in range.
    Returns:
        (list) values from key range
    """
    if tree is None:
        return []
    if tree.key > lo:
        range_search(tree.left, lo, hi)
    if tree.key >= lo and tree.key < hi:
        accum.append(tree.val)
    if tree.key < hi:
        range_search(tree.right, lo, hi)
    return accum
