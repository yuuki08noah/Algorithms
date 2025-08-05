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

    def insert(self, data, node: Node = None):
        if self.root is None:
            self.root = Node(data)
            return self.root
        if not node:
            node = self.root

        if data < node.data:
            if node.left:
                self.insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert(data, node.right)
            else:
                node.right = Node(data)
        node.height = 1 + self.get_height(node.left) + self.get_height(node.right)
        self.validate(node, data)

    def validate(self, node: Node, data):
        print(self.balance_factor(node), node.data)
        if self.balance_factor(node) > 1 and data < node.left.data:
            print(self.root.data, node.data, self.root==node)
            if self.root == node:
                node = self.right_rotate(node)
                self.root = node
            else:
                node = self.right_rotate(node)
        elif self.balance_factor(node) < -1 and data > node.right.data:
            print(self.root.data, node.data, self.root==node)
            if self.root == node:
                node = self.left_rotate(node)
                self.root = node
            else:
                node = self.left_rotate(node)
        elif self.balance_factor(node) > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            if self.root == node:
                node = self.right_rotate(node)
                self.root = node
            else:
                node = self.right_rotate(node)
        elif self.balance_factor(node) < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            if self.root == node:
                node = self.left_rotate(node)
                self.root = node
            else:
                node = self.left_rotate(node)

    def successor_left(self, node: Node):
        while node.left:
            node = node.left
        return node

    def successor_right(self, node: Node):
        while node.right:
            node = node.right
        return node

    def right_rotate(self, node: Node):
        mid = node.left
        node.left = mid.right
        mid.right = node
        return mid

    def left_rotate(self, node: Node):
        mid = node.right
        node.right = mid.left
        mid.left = node
        return mid

    def preorder(self, node: Node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

tree = AVLTree()
while True:
    command = input().strip().split()
    if command[0] == 'i':
        tree.insert(int(command[1]))
    if command[0] == 'p':
        tree.preorder(tree.root)

