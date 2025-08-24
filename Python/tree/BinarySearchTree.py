import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data, left=None, right=None, parent=None, direction=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.direction = direction

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data, node):
        if self.root is None:
            self.root = Node(data, direction='root')
            return self.root
        node = self.root
        temp = None
        while node is not None:
            temp = node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        if data < temp.data:
            temp.left = Node(data, parent=temp, direction="left")
        else:
            temp.right = Node(data, parent=temp, direction="right")

    def search(self, data, node):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return None

    def successor(self, node):
        if node.right is None:
            return node
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    def delete(self, data, node):
        res = self.search(data, self.root)
        if res is None:
            return None
        if res.left is None and res.right is None:
            if res.direction == 'left':
                res.parent.left = None
            elif res.direction == 'right':
                res.parent.right = None
            else:
                self.root = None
        elif res.left is not None and res.right is not None:
            suc = self.successor(res)
            res.data = suc.data
            if suc.direction == 'left':
                suc.parent.left = None
            else:
                if suc.right:
                    suc.parent.right = suc.right
                else:
                    suc.parent.right = None
        else:
            if res.left:
                res.parent.left = res.left
                res.left.parent = res.parent
            else:
                res.parent.right = res.right
                res.right.parent = res.parent

class BST:
    def __init__(self):
        self.root = None

    # 삽입
    def insert(self, data, asdf):
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            # 같으면 아무것도 안 함 (중복 X)
            return node

        self.root = _insert(self.root, data)

    # 탐색
    def search(self, data, node=None):
        if node is None:
            return None
        if data < node.data:
            return self.search(data, node.left)
        elif data > node.data:
            return self.search(data, node.right)
        else:
            return node

    # 삭제
    def delete(self, data, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None

        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            # 삭제할 노드 찾음
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                succ = self._min_value_node(node.right)
                node.data = succ.data
                node.right = self.delete(succ.data, node.right)

        if node == self.root:
            self.root = node
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current