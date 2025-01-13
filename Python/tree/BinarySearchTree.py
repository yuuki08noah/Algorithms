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

    def insert(self, data):
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

    def search(self, data):
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

    def remove(self, data):
        res = self.search(data)
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