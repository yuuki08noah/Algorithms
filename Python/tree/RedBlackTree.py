class Node:
    def __init__(self, data, color="Black", nil = False):
        self.data = data
        self.left = None if nil else nil_node
        self.right = None if nil else nil_node
        self.color = color
        self.nil = nil
        self.extra_black = False

nil_node = Node(None, nil=True)
class RedBlackTree:
    root = None
    def search(self, key, node: Node):
        if node.data is None:
            return node
        if key < node.data:
            return self.search(key, node.left)
        elif key > node.data:
            return self.search(key, node.right)
        else:
            return node

    def insert(self, data, node: Node = None):
        if self.root is None:
            self.root = Node(data, color="Black")
            return self.root
        if not node:
            node = self.root

        if data < node.data:
            if node.left and not node.left.nil:
                node.left = self.insert(data, node.left)
            else:
                node.left = Node(data, color="Red")
        elif data > node.data:
            if node.right and not node.right.nil:
                node.right = self.insert(data, node.right)
            else:
                node.right = Node(data, color="Red")
        node = self.validate_insert(node)
        if node == self.root:
            if node.color == "Red":
                node.color = "Black"
                self.root = node
                return node
        return node

    def delete(self, key, node: Node = None):
        if node is None or node.data is None:
            return node
        if key < node.data:
            node.left = self.delete(key, node.left)
            node = self.validate_delete(node)
            if node == self.root and node.color == "Red":
                node.color = "Black"
                self.root = node
            return node
        elif key > node.data:
            node.right = self.delete(key, node.right)
            node = self.validate_delete(node)
            if node == self.root and node.color == "Red":
                node.color = "Black"
                self.root = node
            return node
        else:
            has_left = node.left and not node.left.nil
            has_right = node.right and not node.right.nil

            if has_left and has_right:
                # 후계자 값 복사 후, 오른쪽에서 그 키를 삭제
                succ = self.successor(node)
                node.data = succ.data
                node.right = self.delete(succ.data, node.right)
                node = self.validate_delete(node)
                if node == self.root and node.color == "Red":
                    node.color = "Black"
                    self.root = node
                return node
            else:
                # 0~1 자식: 자식으로 치환 반환
                child = node.left if has_left else node.right
                if not child or child.nil:
                    child = nil_node

                # RB 특성 복구용 extra_black 전파
                if node.color == "Black":
                    if child.color == "Red":
                        child.color = "Black"
                    else:
                        child.extra_black = True

                return child

    def validate_delete(self, parent: Node):
        if not parent: return nil_node
        if parent.left.extra_black and parent.left.color == "Black" and parent.right.color == "Black":
            if parent.right.right and parent.right.right.color == "Red":
                parent.right.color = parent.color
                parent.right.right.color = "Black"
                parent.color = "Black"
                parent = self.left_rotate(parent)
            elif parent.right.left and parent.right.left.color == "Red" \
                    and parent.right.right and  parent.right.right.color == "Black":
                parent.right, parent.right.left = self.color_swap(parent.right, parent.right.left)
                parent.right = self.right_rotate(parent.right)
                parent.right.color = parent.color
                parent.color = "Black"
                parent.right.right.color = "Black"
                parent = self.left_rotate(parent)
            elif parent.right.left and parent.right.left.color == "Black" \
                and parent.right.right and parent.right.right.color == "Black":
                parent.extra_black = True
                parent.right.color = "Red"
            parent.left.extra_black = False
        elif parent.right.extra_black and parent.left.color == "Black":
            if parent.left.left and parent.left.left.color == "Red":
                parent.left.color = parent.color
                parent.left.left.color = "Black"
                parent.color = "Black"
                parent = self.right_rotate(parent)
            elif parent.left.right and parent.left.right.color == "Red" \
                 and parent.left.left and parent.left.left.color == "Black":
                parent.left, parent.left.right = self.color_swap(parent.left, parent.left.right)
                parent.left = self.left_rotate(parent.left)
                parent.left.color = parent.color
                parent.color = "Black"
                parent.left.left.color = "Black"
                parent = self.right_rotate(parent)
            elif parent.left.right and parent.left.right.color == "Black" \
                and parent.left.left and parent.left.left.color == "Black":
                parent.extra_black = True
                parent.left.color = "Red"
            parent.right.extra_black = False
        elif parent.left.extra_black and parent.right.color == "Red":
            parent, parent.right = self.color_swap(parent, parent.right)
            parent = self.left_rotate(parent)
            parent.left = self.validate_delete(parent.left)
            parent.left.extra_black = False
        elif parent.right.extra_black and parent.left.color == "Red":
            parent, parent.left = self.color_swap(parent, parent.left)
            parent = self.right_rotate(parent)
            parent.right = self.validate_delete(parent.right)
            parent.right.extra_black = False
        if parent == self.root:
            if parent.color == "Red":
                parent.color = "Black"
                self.root = parent
        return parent

    def validate_insert(self, node: Node):
        if node.left.color == "Red":
            if node.left.left.color == "Red" and node.right.color == "Black":
                node, node.left = self.color_swap(node, node.left)
                node = self.right_rotate(node)
            if node.left.right.color == "Red" and node.right.color == "Black":
                node.left = self.left_rotate(node.left)
                node, node.left = self.color_swap(node, node.left)
                node = self.right_rotate(node)
        if node.right.color == "Red":
            if node.right.right.color == "Red" and node.left.color == "Black":
                node, node.right = self.color_swap(node, node.right)
                node = self.left_rotate(node)
            if node.right.left.color == "Red" and node.left.color == "Black":
                node.right = self.right_rotate(node.right)
                node, node.right = self.color_swap(node, node.right)
                node = self.left_rotate(node)
        if node.right.color == "Red" and node.left.color == "Red":
            if node.right.right.color == "Red" or node.right.left.color == "Red" \
                or node.left.left.color == "Red" or node.left.right.color == "Red":
                node.color = "Red"
                node.left.color = "Black"
                node.right.color = "Black"
        return node

    def color_swap(self, node1: Node, node2: Node):
        tmp = node1.color
        node1.color = node2.color
        node2.color = tmp
        return node1, node2

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

    def successor(self, node: Node):
        if node.right and not node.right.nil:
            node = node.right
            while node.left and not node.left.nil:
                node = node.left
        return node

    def preorder(self, node: Node):
        if node:
            print(node.data, node.color, node.extra_black)
            self.preorder(node.left)
            self.preorder(node.right)

# tree = RedBlackTree()
# while True:
#     command = input().strip().split()
#     if command[0] == 'i':
#         tree.root = tree.insert(int(command[1]))
#     if command[0] == 'p':
#         tree.preorder(tree.root)
#     if command[0] == 'd':
#         tree.root = tree.delete(int(command[1]))
#     if command[0] == 'q':
#         print(tree.root.data)
