from math import inf

from Python.exceptions.EmptyException import EmptyException
from Python.exceptions.FullExeption import FullException


class MaxHeap:
    def __init__(self, size):
        self.heap = [-inf] * (size + 1)
        self.top = 0
        self.size = size

    def insert(self, key):
        self.top += 1
        if self.top >= self.size:
            raise FullException("Heap")
        self.heap[self.top] = key
        point = self.top
        while point != 1 and self.heap[point] > self.heap[point // 2]:
            self.heap[point], self.heap[point // 2] = self.heap[point // 2], self.heap[point]
            point = point // 2
        return key

    def pop(self):
        if self.top < 1:
            raise EmptyException("Heap")
        res = self.heap[1]
        self.heap[1] = self.heap[self.top]
        self.top -= 1
        point = 1
        while point != self.top and (self.heap[point] < self.heap[point*2] or self.heap[point] < self.heap[point*2+1]):
            if self.heap[point*2] < self.heap[point*2+1]:
                self.heap[point], self.heap[point*2+1] = self.heap[point*2+1], self.heap[point]
                point = point*2 + 1
            else:
                self.heap[point], self.heap[point*2] = self.heap[point*2], self.heap[point]
                point = point*2
        return res