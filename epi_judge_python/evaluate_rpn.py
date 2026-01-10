from test_framework import generic_test
from collections import deque

operators = set(["+", "-", "*", "/"])

def flush(operator, first, second):
    match operator:
        case "+":
            return int(first)+int(second)
        case "-":
            return int(first)-int(second)
        case "*":
            return int(first)*int(second)
        case "/":
            return int(first)/int(second)

def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    ops = deque(expression.split(","))
    print(expression)
    expr = []
    while len(ops):
        operand = ops.popleft()
        if operand in operators:
            second, first = expr.pop(), expr.pop()
            product = flush(operand, first, second)
            ops.appendleft(product)
        else:
            expr.append(operand)

    return int(expr[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
