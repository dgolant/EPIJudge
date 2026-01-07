import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    len0 = len1 = 0
    d0 = l0
    d1 = l1

    while l0:
        len0+=1
        l0 = l0.next

    while l1:
        len1+=1
        l1 = l1.next

    diff = abs(len1-len0)
    if len1 > len0:
        for _ in range(diff):
            d1 = d1.next
    else:
        for _ in range(diff):
            d0 = d0.next

    while d0 and d1:
        if d0 == d1:
            return d0
        d0 = d0.next
        d1 = d1.next

    return None

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
