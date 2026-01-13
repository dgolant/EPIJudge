from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def check_symmetric(s1: BinaryTreeNode, s2: BinaryTreeNode):
    if not s1 and not s2:
      return True
    elif s1 and s2:
      if s1.data != s2.data:
         return False
      else:
        return check_symmetric(s1.left, s2.right) and check_symmetric(s1.right, s2.left)
    return False
      

def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if not tree:
       return True
    return check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
