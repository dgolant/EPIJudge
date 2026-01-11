from test_framework import generic_test


def snake_string(s: str) -> str:
    i = 1
    res = []
    # top
    while i < len(s):
        res.append(s[i])
        i+=4
    # mid 
    i = 0
    while i < len(s):
        res.append(s[i])
        i+=2    
    # bottom
    i=3
    while i< len(s):
        res.append(s[i])
        i+=4
    
    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
