from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.data = [None]*capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        return

    def enqueue(self, x: int) -> None:
        if self.tail >= self.capacity:
            self.data.append([None]*self.capacity)
            self.data[self.tail] = x
        else:
            self.data[self.tail] = x
        
        self.tail+=1
        return

    def dequeue(self) -> int:
        res = self.data[self.head]
        self.data[self.head] = None
        self.head+=1
        return res

    def size(self) -> int:
        return self.tail-self.head


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
