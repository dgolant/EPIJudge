from test_framework import generic_test
from test_framework.test_failure import TestFailure

string_int_map = {
    "0": 0,
    "1": 1, 
    "2": 2,
    "3": 3, 
    "4": 4,
    "5": 5, 
    "6": 6,
    "7": 7, 
    "8": 8,
    "9": 9, 
    "-": -1,
}

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
      output.append(int_string_map[lsb])
      # drop the least significant digit
      input//=10
    if x < 0:
        # swap the final digit magnitude
        output[-1]= "-"+output[-1]
    res = "".join(reversed(output))
    return res



def string_to_int(s: str) -> int:
    res=0
    mag=1
    for c in reversed(s):
        if c == "+":
            continue
        i = string_int_map[c]
        if i != -1:
          adder = i*mag
          res+=adder
        else:
            # we know we're on the last index so this is safe
            res*=-1
        mag*=10
    return res


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
