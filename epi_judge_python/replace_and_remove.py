import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# b,a,c,b,c,b,-,-,-,-,-
# a,c,c,_,b,-,-,-,-,-                             1
def replace_and_remove(size: int, s: List[str]) -> int:
    write_head, a_count = 0,0
    # iterate forward and delete b's, count a's
    for i in range(size):
        char = s[i]
        if char != 'b':
            s[write_head] = char
            write_head+=1
        if char == 'a':
          a_count+=1
    # iterate backward and replace A's
    cur_index=write_head-1
    write_head+=a_count-1
    final_size = write_head+1
    while cur_index >=0:
        if s[cur_index] == 'a':
            s[write_head-1:write_head+1] = 'dd'
            write_head-=2
        else:
            s[write_head] = s[cur_index]
            write_head-=1
        cur_index-=1

      
    return final_size

# bdcabadbdbbadccadadddbcc
# dcaaddadccadadddcc
# dcaaddadccadadddcc
# dcdddddddddccddddddddcc
# dcddddddddcdccddddcdddcc

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
