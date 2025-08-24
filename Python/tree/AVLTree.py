class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree:
    root = None

    def get_height(self, node: Node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node: Node):
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node: Node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def search(self, key, node: Node = None):
        if not node:
            return None
        if key < node.data:
            return self.search(key, node.left)
        elif key > node.data:
            return self.search(key, node.right)
        else:
            return node

    def insert(self, data, node: Node = None):
        if self.root is None:
            self.root = Node(data)
            return self.root
        if not node:
            node = self.root

        if data < node.data:
            if node.left:
                node.left =  self.insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                node.right = self.insert(data, node.right)
            else:
                node.right = Node(data)
        self.update_height(node)
        return self.validate(node, data)

    def delete(self, key, node: Node = None):
        if node is None:
            return
        if key < node.data:
            node.left = self.delete(key, node.left)
        elif key > node.data:
            node.right = self.delete(key, node.right)
        else:
            if not node.left or not node.right:
                node = node.left or node.right
            else:
                suc = self.successor(node.right)
                node.data = suc.data
                node.right = self.delete(suc.data, node.right)
        if not node: return node
        self.update_height(node)
        return self.validate(node, key)

    def validate(self, node: Node, data):
        if self.balance_factor(node) > 1 and data < node.left.data:
            node = self.right_rotate(node)
        elif self.balance_factor(node) < -1 and data > node.right.data:
            node = self.left_rotate(node)
        elif self.balance_factor(node) > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        elif self.balance_factor(node) < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        self.update_height(node)
        return node

    def successor(self, node: Node):
        while node.left:
            node = node.left
        return node

    def right_rotate(self, node: Node):
        mid = node.left
        if not mid: return node
        node.left = mid.right
        mid.right = node
        self.update_height(node)
        self.update_height(mid)
        return mid

    def left_rotate(self, node: Node):
        mid = node.right
        if not mid: return node
        node.right = mid.left
        mid.left = node
        self.update_height(node)
        self.update_height(mid)
        return mid

    def preorder(self, node: Node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

# tree = AVLTree()
# while True:
#     command = input().strip().split()
#     if command[0] == 'i':
#         tree.root = tree.insert(int(command[1]))
#     if command[0] == 'd':
#         tree.root = tree.delete(int(command[1]), tree.root)
#     if command[0] == 'p':
#         tree.preorder(tree.root)
#
