import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_range(s, start, end):
    # reverse everything between word_Start and the current char (space)
    s[start:end] = s[start:end][::-1]


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # reverse the whole range
    # o(n) t, o(1) space
    s.reverse()
    # but now the words are all backwards too. So we reverse the substrings
    word_start = 0 # can we assume this? 
    for i in range(len(s)):
        # print(s)
        if s[i] == ' ':
            reverse_range(s, word_start, i)
            word_start = i+1
    reverse_range(s, word_start, len(s))
    # print(f"s is now {s}, start: {word_start}, end: ")
    return


# o(N) time, o(n) space


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
