from copy import copy
from typing import List

class Node:
    val: int
    left = None
    right = None
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class DynamicSegmentTree:
    nodes: List[Node] = []
    roots = []
    size = 0

    def __init__(self, arr):
        self.size = 1
        self.root = Node()
        self.build(self.root, 1, len(arr)-1, arr)

    def build(self, node, start, end, arr):
        if start == end:
            node.val = arr[start]
            return node
        mid = (start + end) // 2
        node.left = self.build(Node(), start, mid, arr)
        node.right = self.build(Node(), mid+1, end, arr)
        node.val = node.left.val + node.right.val
        return node

    def update(self, node, start, end, idx, val):
        node = copy(node)
        if end < idx or idx < start: return
        if start == end:
            node.val = val
            return node
        mid = (start + end) // 2
        if idx <= mid:
            if not node.left:
                node.left = Node()
            node.left = self.update(node.left, start, mid, idx, val)
        else:
            if not node.right:
                node.right = Node()
            node.right = self.update(node.right, mid+1, end, idx, val)

        v1 = node.left.val if node.left else 0
        v2 = node.right.val if node.right else 0
        node.val = v1 + v2
        return node

    def query(self, node, start, end, left, right):
        if not node: return 0
        if right < start or end < left: return 0
        if left <= start and end <= right: return node.val
        mid = (start + end) // 2
        return self.query(node.left, start, mid, left, right) + self.query(node.right, mid+1, end, left, right)

n = int(input())
arr = [0] + list(map(int, input().split()))
tree = DynamicSegmentTree(arr)
tree.roots.append(tree.root)
m = int(input())
for i in range(m):
    l = list(map(int, input().split()))
    if l[0] == 1:
        tree.root = tree.update(tree.root, 1, n, l[1], l[2])
        tree.roots.append(tree.root)
    else:
        print(tree.query(tree.roots[l[1]], 1, n, l[2], l[3]))

