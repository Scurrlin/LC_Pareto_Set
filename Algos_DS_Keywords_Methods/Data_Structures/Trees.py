# Trees

# A tree is a hierarchical data structure consisting of nodes, with a single
# node as the root. Each node has zero or more child nodes, and nodes with no
# children are called leaf nodes.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
