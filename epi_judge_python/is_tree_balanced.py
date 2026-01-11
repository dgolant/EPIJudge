from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_balanced_inner(node: BinaryTreeNode) -> int | bool:
    if not node:
        return -1, True
    left_height, left_bal = is_balanced_inner(node.left)
    right_height, right_bal = is_balanced_inner(node.right)
    height = max(left_height, right_height)+1
    balanced = left_bal and right_bal and abs(left_height-right_height) <=1
    return height, balanced

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    left_height, left_balance = is_balanced_inner(tree.left)
    right_height, right_balance = is_balanced_inner(tree.right)
    if not left_balance or not right_balance:
        return False
    return abs(left_height-right_height) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
