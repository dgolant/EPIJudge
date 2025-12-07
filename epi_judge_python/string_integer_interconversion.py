from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

int_string_map = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    -1: "-",
}


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    
    input = abs(x)
    output = []

    while input > 0:
      lsb = input%10
      # x%10 gives the LSB of x, ord('0') is the integer code point for '0', so joining them is saying "give me the integer for the char 0, and then offset that by LSB of x"
      # chr turns that back into a char
      output.append(chr(ord('0')+x%10))
      # drop the least significant digit
      input//=10
    
    if x < 0:
        # swap the final digit magnitude
        output[-1]= "-"+output[-1]
    res = "".join(reversed(output))
    return res


# "+4253"
def string_to_int(s: str) -> int:
    res=0
    mag=1
    valence = -1 if s[0] == "-" else 1

    for c in s:
        if c in "-+":
            continue
        res*=10
        res+=string.digits.index(c)
    return res*valence
    


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
