from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
      return []
    
    stack = [tree]
    res = []

    while stack:
       node = stack.pop()
       res.append(node.data)
       if node.left:
          stack.append(node.left)
       if node.right:
          stack.append(node.right)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
