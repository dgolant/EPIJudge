from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def traverse_until(L: ListNode, target: int):
    for i in range(target-2):
        L = L.next
    return L

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    # start is 1-based, and we go to the node right before start
    for _ in range(1, start):
        sublist_head = sublist_head.next


    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
