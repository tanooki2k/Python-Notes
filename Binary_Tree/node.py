class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.row = 0

    def __repr__(self):
        return f'<Node {self.value}>'
