# BST

# A binary search tree is a binary tree with the additional property that for
# every node, the value of all the nodes in the left subtree is less than the
# node's value, and the value of all the nodes in the right subtree is greater
# than the node's value.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

root = TreeNode(5)
root = insert(root, 3)
root = insert(root, 7)
