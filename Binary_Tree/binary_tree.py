from node import Node


class BinaryTree:
    separator = "\t"

    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        index = 0
        while current_node:
            index += 1
            if new_node.value == current_node.value:
                raise ValueError("A node with that value already exists.")
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    new_node.row = index
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    new_node.row = index
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f'A node with value {value} was not found.')

    def inorder(self):
        self._inorder_recursive(self.head)

    def preorder(self):
        self._preorder_recursive(self.head)

    def postorder(self):
        self._postorder_recursive(self.head)

    def find_parent(self, value: int):
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or \
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

    @staticmethod
    def find_rightmost(node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            self.delete_node_with_two_children(to_delete, to_delete_parent)
        elif to_delete.left or to_delete.right:
            self.delete_node_with_a_child(to_delete, to_delete_parent)
        else:
            self.delete_node_with_no_children(to_delete, to_delete_parent)

    def delete_node_with_two_children(self, to_delete, to_delete_parent):
        rightmost = self.find_rightmost(to_delete.left)
        rightmost_parent = self.find_parent(rightmost.value)

        self._correct_row(rightmost.left, rightmost.row)
        if rightmost_parent != to_delete:
            rightmost_parent.right = rightmost.left
            rightmost.left = to_delete.left
        rightmost.right = to_delete.right

        if to_delete == to_delete_parent.left:
            to_delete_parent.left = rightmost
            to_delete_parent.left.row = to_delete.row
        elif to_delete == to_delete_parent.right:
            to_delete_parent.right = rightmost
            to_delete_parent.right.row = to_delete.row
        else:
            self.head = rightmost
            self.head.row = to_delete.row

    def delete_node_with_a_child(self, to_delete, to_delete_parent):
        if to_delete == to_delete_parent.left:
            to_delete_parent.left = to_delete.left or to_delete.right
            to_delete_parent.left.row = to_delete.row
        elif to_delete == to_delete_parent.right:
            to_delete_parent.right = to_delete.left or to_delete.right
            to_delete_parent.right.row = to_delete.row
        else:
            self.head = to_delete.left or to_delete.right
            self.head.row = to_delete.row

    def delete_node_with_no_children(self, to_delete, to_delete_parent):
        if to_delete == to_delete_parent.left:
            to_delete_parent.left = None
        elif to_delete == to_delete_parent.right:
            to_delete_parent.right = None
        else:
            self.head = None

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(self.separator * current_node.row, current_node)
        self._inorder_recursive(current_node.right)

    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(self.separator * current_node.row, current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

    def _postorder_recursive(self, current_node):
        if not current_node:
            return
        self._postorder_recursive(current_node.left)
        self._postorder_recursive(current_node.right)
        print(self.separator * current_node.row, current_node)

    def _correct_row(self, current_node, row):
        if not current_node:
            return

        current_node.row = row
        self._correct_row(current_node.left, row - 1)
        self._correct_row(current_node.right, row - 1)
