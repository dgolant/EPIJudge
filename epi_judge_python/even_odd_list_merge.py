from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    lists, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        lists[turn].next = L
        lists[turn] = lists[turn].next

        L = L.next
        turn = 1 if turn == 0 else 0

    lists[1].next = None
    lists[0].next = odd_dummy_head.next

    return even_dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
