class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:

            # Base case: return if node is None
            return None
        
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively invert left subtree
        self.invertTree(root.left)

        # Recursively invert right subtree
        self.invertTree(root.right)
        
        # Return the root of the inverted tree
        return root

# Time Complexity: O(N)
# Space Complexity: O(H)