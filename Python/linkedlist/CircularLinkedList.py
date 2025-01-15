from Python.exceptions.EmptyException import EmptyException
from Python.linkedlist.Node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head_insert(data)
            return
        temp = self.head.next
        node = Node(data, self.head)
        while temp.next != self.head:
            temp = temp.next
        temp.next = node
        self.size += 1

    def insert(self, data):
        if self.head is None:
            self.head_insert(data)
            return
        node = Node(data, self.head.next)
        self.head.next = node
        self.size += 1

    def delete(self):
        if self.head is None:
            raise EmptyException("List is empty")
        self.head.next = self.head.next.next
        self.size -= 1

    def head_insert(self, data):
        self.head = Node(data)
        self.head.next = self.head
        self.size += 1

    def print(self):
        if self.head is None:
            raise EmptyException("List is empty")

        node = self.head.next
        print(self.head.data, end=" -> ")
        while node != self.head:
            print(node.data, end=" -> ")
            node = node.next
