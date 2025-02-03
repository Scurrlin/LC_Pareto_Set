class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Stores the maximum diameter
        res = 0

        def dfs(root):

            # Allows modification of `res` inside the nested function
            nonlocal res

            if not root:

                # Base case: height of an empty tree is 0
                return 0
            
            # Compute height of left subtree
            left = dfs(root.left)

            # Compute height of right subtree
            right = dfs(root.right)

            # Update max diameter (longest path)
            res = max(res, left + right)

            # Return height of current node
            return 1 + max(left, right)

        # Start DFS from the root
        dfs(root)

        # Return the maximum diameter found
        return res

# Time Complexity: O(N)
# Space Complexity: O(H)