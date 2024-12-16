from Exceptions.EmptyException import EmptyException
from Exceptions.FullExeption import FullException


class Stack:
    def __init__(self, size):
        self.items = [None for _ in range(size)]
        self.size = size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.isFull():
            raise FullException("Stack")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.isEmpty():
            raise EmptyException("Stack")
        result = self.items[self.top]
        self.top -= 1
        return result

    def peek(self):
        if self.isEmpty():
            raise EmptyException("Stack")
        return self.items[self.top]

    def getSize(self):
        return self.size

    def clear(self):
        top = -1

    def contains(self, item):
        if self.isEmpty():
            raise EmptyException("Stack")
        for i in self.items:
            if i == item: return True
        return False
