from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False
    print(f"tree data:{tree.data}, remaining_weight:{remaining_weight}")
    # if remaining_weight-tree.data > 0:
    #     return False
    print("--------")
    if remaining_weight-tree.data == 0:
        return True
    return has_path_sum(tree.left, remaining_weight-tree.data) or has_path_sum(tree.right, remaining_weight-tree.data)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
