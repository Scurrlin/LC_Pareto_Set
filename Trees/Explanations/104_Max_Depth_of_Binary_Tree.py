class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:

            # Base case: an empty tree has depth 0
            return 0
        
        # Recursion on left subtree
        left_depth = self.maxDepth(root.left)
        
        # Recurion on right subtree
        right_depth = self.maxDepth(root.right)
        
        # Return the max depth of both subtrees + 1 for the root
        return max(left_depth, right_depth) + 1

# Time Complexity: O(N)
# Space Complexity: O(H)